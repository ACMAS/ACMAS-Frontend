from django.contrib import admin

from .models import (
    Course,
    FileModerationQueue,
    Question,
    QuestionModerationQueue,
    University,
    UploadedFile,
    User,
)


def approve_files(modeladmin, request, queryset):
    short_description:str
    for file in queryset:
        file.toFile().save()
        file.delete()


def reject_files(modeladmin, request, queryset):
    short_description:str
    for file in queryset:
        file.delete()


def approve_questions(modeladmin, request, queryset):
    short_description:str
    for question in queryset:
        question.toQuestion().save()
        question.delete()


def reject_questions(modeladmin, request, queryset):
    short_description:str
    for question in queryset:
        question.delete()


class FileModerationQueueAdmin(admin.ModelAdmin):
    actions = [approve_files, reject_files]


class QuestionModerationQueueAdmin(admin.ModelAdmin):
    actions = [approve_questions, reject_questions]


admin.site.register(Question)
admin.site.register(University)
admin.site.register(Course)
admin.site.register(UploadedFile)
admin.site.register(User)
admin.site.register(FileModerationQueue, FileModerationQueueAdmin)
admin.site.register(QuestionModerationQueue, QuestionModerationQueueAdmin)


class MyModelAdmin(admin.ModelAdmin):
    actions = [approve_files, reject_files, approve_questions, reject_questions]
    approve_files.short_description = "Approve selected file(s)"
    reject_files.short_description = "Reject selected file(s)"
    approve_questions.short_description = "Approve selected question(s)"
    reject_questions.short_description = "Reject selected question(s)"


admin.site.site_header = "ACMAS Admin"
admin.site.site_title = "ACMAS Admin Portal"
admin.site.index_title = "Welcome to the ACMAS Administration Portal"
