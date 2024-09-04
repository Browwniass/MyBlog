from rest_framework import serializers
from .models import *
from taggit.serializers import (TagListSerializerField,
                                TaggitSerializer)
from taggit.models import Tag


class ArticleSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()

    class Meta:
        model = Article
        fields = "__all__"
        read_only_fields = ['created_at', 'updated_at']
    

class MyTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'slug']