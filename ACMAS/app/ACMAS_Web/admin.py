from django.contrib import admin

from .models import Course, Question, University, UploadedFile, User

admin.site.register(Question)
admin.site.register(University)
admin.site.register(Course)
admin.site.register(UploadedFile)
admin.site.register(User)

admin.site.site_header = "ACMAS Admin"
admin.site.site_title = "ACMAS Admin Portal"
admin.site.index_title = "Welcome to ACMAS Portal"
