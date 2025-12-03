from django.contrib import admin
from .models import *

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date')
    list_filter= ('author', 'date')

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    list_filter= ('name', 'email')







admin.site.register(Post, PostAdmin)
admin.site.register(Author, AuthorAdmin)