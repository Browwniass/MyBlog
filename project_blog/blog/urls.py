from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import ArticleModelView, Logout, TagsModelView
from rest_framework.authtoken import views


router = routers.SimpleRouter()
router.register('articles', ArticleModelView)
router.register('tags', TagsModelView)

urlpatterns = [
    path("", include(router.urls)),
    path('token-auth/', views.obtain_auth_token, name='api-token-auth'),
    path('logout/', Logout.as_view()),
]