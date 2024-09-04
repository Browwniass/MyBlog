from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import ArticleModelView, TagsModelView


router = routers.SimpleRouter()
router.register('articles', ArticleModelView)
router.register('tags', TagsModelView)

urlpatterns = [
    path('', include(router.urls))
]