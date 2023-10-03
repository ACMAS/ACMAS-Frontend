from django.contrib import admin

# Register your models here.
from .models import Question, University, Course, UploadedFile, User

admin.site.register(Question)
admin.site.register(University)
admin.site.register(Course)
admin.site.register(UploadedFile)
admin.site.register(User)

#Headers for admin page
admin.site.site_header = "ACMAS Admin"
admin.site.site_title = "ACMAS Admin Portal"
admin.site.index_title = "Welcome to ACMAS Portal"
