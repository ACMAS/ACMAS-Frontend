from django.contrib import admin

from .models import Course, Question, University, UploadedFile, User, FileModerationQueue, QuestionModerationQueue

admin.site.register(Question)
admin.site.register(University)
admin.site.register(Course)
admin.site.register(UploadedFile)
admin.site.register(User)

#add action to approve files in moderation queue
def approve_files(modeladmin, request, queryset):
    for file in queryset:
        file.toFile().save()
        file.delete()

approve_files.short_description = "Approve selected files"

#add action to reject files in moderation queue
def reject_files(modeladmin, request, queryset):
    for file in queryset:
        file.delete()

reject_files.short_description = "Reject selected files"

class FileModerationQueueAdmin(admin.ModelAdmin):
    actions = [approve_files, reject_files]

admin.site.register(FileModerationQueue, FileModerationQueueAdmin)


#add action to approve questions in moderation queue
def approve_questions(modeladmin, request, queryset):
    for question in queryset:
        question.toQuestion().save()
        question.delete()
    
approve_questions.short_description = "Approve selected questions"

#add action to reject questions in moderation queue
def reject_questions(modeladmin, request, queryset):
    for question in queryset:
        question.delete()

reject_questions.short_description = "Reject selected questions"

class QuestionModerationQueueAdmin(admin.ModelAdmin):
    actions = [approve_questions, reject_questions]

admin.site.register(QuestionModerationQueue, QuestionModerationQueueAdmin)


admin.site.site_header = "ACMAS Admin"
admin.site.site_title = "ACMAS Admin Portal"
admin.site.index_title = "Welcome to the ACMAS Administration Portal"
