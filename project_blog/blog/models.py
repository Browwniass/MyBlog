from django.db.models import Model, CharField, TextField, FileField, DateTimeField  


class Article(Model):
    title = CharField(max_length=100)
    contents = TextField()
    files = FileField(upload_to ='uploads/PostsImages')
    tags = CharField(max_length=255, blank=True, null=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.title}"


