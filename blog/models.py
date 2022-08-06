from django.db import models
from django.conf import settings

# content of post
class Tag(models.Model):
    value = models.TextField(max_length=100)

    def __str__(self):
        return self.value

class Post(models.Model):#metadata and contents of post
    #auth user model from settings class
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    #add system time stamp to post
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True, null=True)
    title = models.TextField(max_length=100)
    slug = models.SlugField() #user friendly path from URI
    summary = models.TextField(max_length=500)
    content = models.TextField()
    tags = models.ManyToManyField(Tag, related_name="posts")

    def __str__(self):
        return self.title