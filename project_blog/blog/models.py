from django.db.models import Model, CharField, TextField, FileField, DateTimeField  
from taggit.managers import TaggableManager


class Article(Model):
    title = CharField(max_length=100)
    contents = TextField()
    files = FileField(upload_to ='uploads/PostsImages', blank=True, null=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    
    tags = TaggableManager()
    
    class Meta:
        ordering = ('-created_at', 'title')
        
    def __str__(self):
        return f"{self.title}"


