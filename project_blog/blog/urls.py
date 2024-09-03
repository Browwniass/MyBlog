from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import ArticleModelView


router = routers.SimpleRouter()
router.register('articles', ArticleModelView)

urlpatterns = [
    path("", include(router.urls))
]