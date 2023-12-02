from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

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

class UploadedFileAdmin(admin.ModelAdmin):
    list_display = ('filename', 'file_dir', 'course', 'date_uploaded', 'flag', 'download', 'openPDF')

    def download(self, obj):
        url = reverse('download_file', kwargs={'pk': obj.pk})
        return format_html('<a href="{}">Download</a>', url)
    download.short_description = 'Download File'

    def openPDF(self, obj):
        url = reverse('pdfReader', kwargs={'url': obj.filename})
        return format_html('<a href="{}">Open PDF</a>', url)
    openPDF.short_description = 'Open PDF'


admin.site.register(Question)
admin.site.register(University)
admin.site.register(Course)
admin.site.register(UploadedFile, UploadedFileAdmin)
admin.site.register(User)
admin.site.register(ModerationQueue, ModerationQueueAdmin)


admin.site.site_header = "ACMAS Admin"
admin.site.site_title = "ACMAS Admin Portal"
admin.site.index_title = "Welcome to the ACMAS Administration Portal"
