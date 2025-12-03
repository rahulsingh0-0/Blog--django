from django.urls import path
from . import views
urlpatterns = [
    path("", views.Home, name="home"),
    path("posts/", views.Posts, name="posts"),
    path("posts/<int:id>/", views.PostDetail, name="post_detail"),
]
