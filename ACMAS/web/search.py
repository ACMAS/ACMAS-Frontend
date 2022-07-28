from .models import Course, Question, University, UploadedFile


class searchFacade:
    def __init__(self):
        self.courseFiles = None
        self.courseSearch = None
        self.questionSearch = None

    def getQuery(self):
        return self.courseFiles

    def search(self, uni, course, fType):

        if self.courseSearch is None:
            self.courseSearch = courseSearchHandler(uni, course, fType)
        elif (
            self.courseSearch.uni == uni
            and self.courseSearch.course == course
            and self.courseSearch.fType == fType
        ):
            print("Returning cached files")
            return self.courseFiles

        if uni is None:
            raise ValueError("No University provided")

        self.courseFiles = self.courseSearch.getFiles(uni, course, fType)

        return self.courseFiles

    def searchQuestion(self, question):
        self.questionSearch = self.questionSearch
        self.questionFiles = self.questionFiles
        if self.questionSearch is None:
            self.questionSearch = questionSearchHandler(question)
        elif self.questionSearch.question == question:
            print("Returning cached question")
            return self.questionFiles

        if question is None:
            raise ValueError("No question provided")

        self.questionFiles = questionSearch.getFiles(question)

        return self.questionFiles


class courseSearchHandler:
    def __init__(self, uni, course, fType):
        self.uni = uni
        self.course = course
        self.fType = fType
        self.fileSearch = None

    def getCourses(self, uni):
        university = University.objects.filter(name=uni)
        if university.exists():
            return Course.objects.filter(university=(university.get(name=uni)))
        return None

    def getFiles(self, uni, course, fType):

        self.uni = uni
        self.course = course
        self.fType = fType

        if self.fileSearch is None:
            self.fileSearch = fileSearchHandler()

        courses = self.getCourses(uni)
        if courses is None:
            return None
        if course is not None:
            return self.fileSearch.getFiles(courses.get(name=course), fType)
        elif courses:
            files = self.fileSearch.getFiles(courses[0], fType)
            for c in courses[1:]:
                files.union(self.fileSearch.getFiles(c, fType)).order_by("name")
            return files
        else:
            return courses


class questionSearchHandler:
    def __init__(self, question):
        self.question = question

    def searchQuestion(self, question):
        return Question.objects.filter(question=question)


class fileSearchHandler:
    def getFiles(self, course, fType):
        if fType == "All":
            return UploadedFile.objects.filter(course=course)
        else:
            return UploadedFile.objects.filter(course=course, flag=fType)

    def getPath(self, name):
        return UploadedFile.objects.get(name=name).file_dir
