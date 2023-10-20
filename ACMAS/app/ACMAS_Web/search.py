from .models import Course, Question, University, UploadedFile
import yake

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
        Parameters: String question - string containing the question that will be getting 
        digested via yake, a keyword extractor that uses an NLP model to glean keywords 
        from a text string
        Returns: QuerySet of Question
        """
        # If no question designated Error (delete?)
        if question is None:
            raise ValueError("No question provided")
        
        #Using Yake
        language = "en"
        max_ngram_size = 1
        deduplication_threshold = 0.9
        #Essentially, roughly half of the words in the original question
        numOfKeywords = 10 # res = (question.count(" ")+1)//2 
        custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, 
            dedupLim=deduplication_threshold, top=numOfKeywords, features=None)
        keywords = custom_kw_extractor.extract_keywords(question)
        for kw in keywords:
            self.searchQuestion(kw[0])
            #^kw[0] gets the word entry in the two-value tuples each keyword has
        return


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
    def __init__(self, question):
        self.question = question

    def searchQuestion(self, question):
        """
        Parameters: String question - string containing the question
        Returns:    QuerySet of Question
        """
        print("TESTING")
        return Question.objects.all() #.filter(question=question)


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
