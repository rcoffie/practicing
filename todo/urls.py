
from django.urls import path
from todo.views import (list_posts,create_post, edit_post, post_detail, delete_post)
urlpatterns = [
    path('list-posts/',list_posts,name="list_posts"),
    path('create-post/', create_post, name="create_post"),
    path('edit-post/<int:id>/', edit_post, name="edit_post"),
    path('post-detail/<int:id>/', post_detail, name="post_detail"),
    path('delete-post/<int:id>/', delete_post, name="delete_post")
]
