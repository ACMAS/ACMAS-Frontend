from django.contrib import admin

# Register your models here.

#Adding models to the site
from django.contrib import admin
from .models import Post

admin.site.register(Post)