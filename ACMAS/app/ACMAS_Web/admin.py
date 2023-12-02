from django.contrib import admin

from .models import (Course, ModerationQueue, Question, University, UploadedFile, User)


def approve(modeladmin, request, queryset):
    for file in queryset:
        file.toFile().save()
        file.delete()


def reject(modeladmin, request, queryset):
    for file in queryset:
        file.delete()


class ModerationQueueAdmin(admin.ModelAdmin):
    actions = [approve, reject]


admin.site.register(Question)
admin.site.register(University)
admin.site.register(Course)
admin.site.register(UploadedFile)
admin.site.register(User)
admin.site.register(ModerationQueue, ModerationQueueAdmin)


admin.site.site_header = "ACMAS Admin"
admin.site.site_title = "ACMAS Admin Portal"
admin.site.index_title = "Welcome to the ACMAS Administration Portal"
