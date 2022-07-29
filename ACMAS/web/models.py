from django.db import models


class Question(models.Model):
    question = models.TextField()
    Answers = models.TextField()
    Hash = models.TextField()

    def __str__(self):
        return self.question


class University(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.TextField()
    code = models.CharField(max_length=20)
    university = models.TextField()
    semster = models.CharField(max_length=30)
    years = models.TextField()
    test_type = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class UploadedFile(models.Model):
    filename = models.CharField(max_length=60)
    file_dir = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_uploaded = models.CharField(max_length=50)
    flag = models.CharField(max_length=80)

    def __str__(self):
        return self.filename


# DEFINE ALL MODELS HERE WITH SPECS
