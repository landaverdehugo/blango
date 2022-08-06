from django.contrib import admin
from blog.models import Tag, Post 

#Register your models here.
admin.site.register(Tag)


#modfy component from Post contents 
class PostAdmin(admin.ModelAdmin): #create subclass ModelAdmin
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Post, PostAdmin)