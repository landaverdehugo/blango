#Register your models here.
from django.contrib import admin
from blog.models import Tag, Post, Comment

#modify component from Post contents 
class PostAdmin(admin.ModelAdmin): #create subclass ModelAdmin
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Post, PostAdmin)