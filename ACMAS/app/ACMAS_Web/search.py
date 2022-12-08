import json
from .models import Course, Question, University, UploadedFile
from elasticsearch import Elasticsearch

# Class handles external interaction with searching
class searchFacade:
    def __init__(self):
        self.courseFiles = None
        self.courseSearch = None
        self.questionSearch = None
        self.questionFiles = None
        self.recentSearch = None

    def getQuery(self, search_type=None):
        # Returns:  Last QuerySet results from any search
        #           If there have been no searches, return None
        if search_type is not None:
            if self.recentSearch == self.courseFiles:
                search_type[0] = False
            elif self.recentSearch == self.questionFiles:
                search_type[0] = True
        return self.recentSearch

    def search(self, uni, course, fType):
        """
        Parameters: String uni      - string of school/university name
                    String course   - string of course/class
                    String fType    - string designating upload type (Assignment, Exam, Practice)
        Returns:    QuerySet of UploadedFile or None
                    If University or Course is invalid or University doesn't have course return None
        """
        # If this class has yet to search, create search handler
        if self.courseSearch is None:
            self.courseSearch = courseSearchHandler(uni, course, fType)
        # Else if previous search is same as current, return previous result
        elif (
            self.courseSearch.uni == uni
            and self.courseSearch.course == course
            and self.courseSearch.fType == fType
        ):
            print("Returning cached files")
            # Set recent query
            self.recentSearch = self.courseFiles
            return self.courseFiles
        # If no university is designated Error (delete this?)
        if uni is None:
            raise ValueError("No University provided")
        # Search for QuerySet
        # Set recent query
        self.courseFiles = self.courseSearch.getFiles(uni, course, fType)
        self.recentSearch = self.courseFiles

        return self.courseFiles

    def searchQuestion(self, question):
        """
        Parameters: String question - string containing the question
        Returns:    QuerySet of Question
        """
        # If this class has yet to search, create search handler
        if self.questionSearch is None:
            self.questionSearch = questionSearchHandler()
        # Else if previous search is same as current, return previous result
        elif self.questionSearch.question == question:
            print("Returning cached question")
            # Set recent query
            self.recentSearch = self.questionFiles
            return self.questionFiles
        # If no question designated Error (delete?)
        if question is None:
            raise ValueError("No question provided")
        # Search for QuerySet
        # Set recent query
        self.questionFiles = self.questionSearch.searchQuestion(question)
        self.recentSearch = self.questionFiles

        return self.questionFiles


class courseSearchHandler:
    def __init__(self, uni, course, fType):
        self.uni = uni
        self.course = course
        self.fType = fType
        self.fileSearch = None

    def getCourses(self, uni):
        """
        Parameters: String uni  - string of school/university name
        Returns:    QuerySet of Course in University
                    If University doesn't exist return None
        """
        university = University.objects.filter(name=uni)
        if university.exists():
            return Course.objects.filter(university=(university.get(name=uni)))
        return None

    def getFiles(self, uni, course, fType):
        """
        Parameters: String uni      - string of school/university name
                    String course   - string of course/class
                    String fType    - string designating upload type (Assignment, Exam, Practice)
        Returns:    QuerySet of UploadedFile or None
                    If University or Course is invalid or University doesn't have course return None
        """

        self.uni = uni
        self.course = course
        self.fType = fType

        if self.fileSearch is None:
            self.fileSearch = fileSearchHandler()
        courses = self.getCourses(uni)

        # If University doesn't exist return None
        if courses is None:
            return None
        # If course is specified
        if course is not None:
            # If course is in University, return file QuerySet, otherwise return None
            if courses.filter(name=course).exists():
                return self.fileSearch.getFiles(courses.get(name=course), fType)
            else:
                return None
        # If course is not specified, and the University has courses, return all files of University
        elif courses:
            files = self.fileSearch.getFiles(courses[0], fType)
            for c in courses[1:]:
                files.union(self.fileSearch.getFiles(c, fType)).order_by("name")
            return files
        else:
            return None


class questionSearchHandler:
    def __init__(self):
        # This host.docker.internal allows for access to localhost outside of the container
        self.elastic_address = "http://host.docker.internal:9200"
        self.question_index_name = "question_index"
        self.es = Elasticsearch(self.elastic_address)
        self.min_question_length_for_fuzzy = 3

        # Only allow searching by question, the question will be preprocessed first
        # The question field will be split and expanded using an ngram from size 2 to 9
        self.mapping = {
          "properties": {
            "question": {
                "type": "text",
                "analyzer": "ngram_token_analyzer",
                "search_analyzer": "search_term_analyzer"
            }
          }
        }

        # The query is lowercased, tokenized, stop words are removed, and ascii folding is performed
        # to convert non-ascii characters to their ascii equivalent
        self.setting = {
          "index": {
            "max_ngram_diff": 7,
            "analysis": {
                "analyzer": {
                    "search_term_analyzer": {
                        "type": "custom",
                        "stopwords": "_none_",
                        "filter": [
                            "lowercase",
                            "asciifolding",
                            "no_stop"
                        ],
                        "tokenizer": "standard"
                    },
                    "ngram_token_analyzer": {
                        "type": "custom",
                        "stopwords": "_none_",
                        "filter": [
                            "lowercase",
                            "asciifolding",
                            "no_stop",
                            "ngram_filter"
                        ],
                        "tokenizer": "standard"
                    }
                },
                "filter": {
                    "no_stop": {
                        "type": "stop",
                        "stopwords": "_none_"
                    },
                    "ngram_filter": {
                        "type": "ngram",
                        "min_gram": "2",
                        "max_gram": "9"
                    }
                }
            }
          }
        }

        # Only create the questions index if it doesn't already exit
        if not self.es.indices.exists(index=self.question_index_name):
          self.es.indices.create(
            index=self.question_index_name,
            mappings=self.mapping,
            settings=self.setting,
            ignore=400 # ignore 400 already exists code
          )


    def addQuestionToIndex(self, question_doc):
        """
        Parameters: A question id (string)
        Returns: None
        """
        self.es.index(index=self.question_index_name, document=question_doc)
            
    def searchQuestion(self, question):
        """
        Parameters: String question - string containing the question
        Returns:    QuerySet of Question
        """
        self.es.indices.refresh(index=self.question_index_name)
        query_for_question = {
            "query": {
                "bool": {
                    "should": [
                        {
                            # Exact phrase matches should be prioritized and ranked higher, +10 score
                            "multi_match": {
                                "query": question,
                                "type": "phrase",
                                "fields": [
                                    "question"
                                ],
                                "boost": 10
                            }
                        },
                        {
                            # Uses Levenshtein to allow for typos within a certain edit distance automatically found
                            # The query is compared against the n-grams generated for each question in the index
                            "multi_match": {
                                "query": question,
                                "type": "most_fields",
                                "fields": [
                                    "question"
                                ],
                                "fuzziness":"AUTO"
                            }
                        }
                    ]
                }
            }
        }

        # Small queries will not use fuzzy search to avoid too many search results
        if question and len(question) < self.min_question_length_for_fuzzy:
          query_for_question['query']['bool']['should'][1]['multi_match']['fuzziness'] = "0"

        # Returns an object detailing the reseults of the search ranked by score
        response = self.es.search(
            index=self.question_index_name,
            body=json.dumps(query_for_question)
        )
        print('response', response)

        files = []
        for hit in response['hits']['hits']:
            file = hit['_source']
            files.append(file)

        return filesi


class fileSearchHandler:
    def getFiles(self, course, fType):
        """
        Parameters: Course model course - Course to search with
                    String fType        - string designating upload type (Assignment, Exam, Practice)
        Returns:    QuerySet of Question
        """
        if fType == "All":
            return UploadedFile.objects.filter(course=course)
        else:
            return UploadedFile.objects.filter(course=course, flag=fType)

    def getPath(self, name):
        """
        Parameters: String name - name of file to get path of
        Returns:    String of file directory of file
        """
        return UploadedFile.objects.get(name=name).file_dir