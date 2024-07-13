from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("create/post/",views.create_post,name="create_post"),
    path("edit/post/<int:pk>/",views.edit_post,name="edit_post"),
    path('post/<int:post_id>/like/', views.like_post, name='like_post'),


]