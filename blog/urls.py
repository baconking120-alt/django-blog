
from django.urls import path
from .views import blog_home, post_list, post_detail

urlpatterns = [
    path("", blog_home, name="blog_home"),
    path("posts/", post_list, name="post_list"),
    path("posts/<int:pk>/", post_detail, name="post_detail"),
]
