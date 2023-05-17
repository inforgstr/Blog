from django.urls import path
from blog import views

urlpatterns = [
    path("", views.home, name="home"),
    path("blog/", views.blog, name='index'),
    path("blog/<int:pk>/", views.blog_detail, name="blog-detail"),
    path("blog/category/<int:pk>/", views.get_category, name="category"),
]
