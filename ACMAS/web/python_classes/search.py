from django.db.models.query import EmptyQuerySet
from ..models import Course, Question, University, UploadedFile


class searchFacade:

	def __init__(self):
		self.courseFiles = None
		self.courseSearch = None

	def getQuery(self):
		return self.courseFiles

	def search(self, uni, course, fType):

		if self.courseSearch == None:
			self.courseSearch = courseSearchHandler(uni, course, fType)
		elif (
			self.courseSearch.uni == uni 
			and self.courseSearch.course == course
			and self.courseSearch.fType == fType
		):
			print("Returning cached files")
			return self.courseFiles

		if(uni==None):
			raise ValueError("No University provided")

		self.courseFiles = self.courseSearch.getFiles(uni, course, fType)

		return self.courseFiles
		

	def searchQuestion(self, question):
		if self.questionSearch == None:
			self.questionSearch = questionSearchHandler(question)
		elif self.questionSearch.question == question:
			print("Returning cached question")
			return self.questionFiles
		
		if question == None:
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

		if(self.fileSearch == None):
			self.fileSearch = fileSearchHandler()

		courses = self.getCourses(uni)
		if courses == None:
			return None
		if(course!=None):
			return self.fileSearch.getFiles(courses.get(name=course), fType)
		elif courses:
			files = self.fileSearch.getFiles(courses[0], fType)
			for c in courses[1:]:
				files.union(self.Search.getFiles(c, fType)).order_by('name')
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



