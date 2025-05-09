from django.urls import path
from app_blog.views import create, list, read
urlpatterns = [
    path('create/', create.view, name='create'),
    path('list/', list.view, name='list'),
    path('read/<int:post_id>/', read.view, name='read')
]