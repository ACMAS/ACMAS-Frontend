from django.db import models


class Question(models.Model):
    filename = models.TextField()
    question = models.TextField()
    Answers = models.TextField()
    flag = models.TextField(default="()")
    Hash = models.TextField()

    def __str__(self):
        return self.question


class University(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Universities"


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

    class Meta:
        verbose_name = "Uploaded File"
        verbose_name_plural = "Uploaded Files"


class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.username
