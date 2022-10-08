from django.db import models


class Question(models.Model):
    File_Name = models.TextField()
    Question = models.TextField()
    Answers = models.TextField()
    Hash = models.TextField()

    def __str__(self):
        return self.Question


class University(models.Model):
    Name = models.CharField(max_length=50)

    def __str__(self):
        return self.Name


class Course(models.Model):
    Name = models.TextField()
    Course_Code = models.CharField(max_length=20)
    University = models.TextField()
    Semester = models.CharField(max_length=30)
    Years = models.TextField()
    Test_Type = models.CharField(max_length=20)

    def __str__(self):
        return self.Name


class UploadedFile(models.Model):
    File_Name = models.CharField(max_length=60)
    File_Dir = models.TextField()
    Course = models.ForeignKey(Course, on_delete=models.CASCADE)
    Date_Uploaded = models.CharField(max_length=50)
    Flag = models.CharField(max_length=80)

    def __str__(self):
        return self.File_Name
