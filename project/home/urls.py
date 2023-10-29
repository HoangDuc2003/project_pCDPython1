from django.urls import path,re_path
from .models import Post
from . import views
from django.views.generic import ListView, DetailView
from .views import UpdateBlog
urlpatterns = [
    path('', ListView.as_view( 
        queryset = Post.objects.all().order_by('-date'),
        template_name = 'home/blog.html',
        context_object_name = 'Post',
        paginate_by = 10), name = 'blog'),
    path("draft/",views.draft,name= 'draft'),
    path('<int:pk>/',views.post, name='post'),
    path("add_blog/", views.add_Blog, name="add_blog"),
    path("delblog/<int:id>", views.DeleteBlog, name="delblog"),
    path("upload/<int:id>/", views.push_draft, name="upload"),
    path("editblog/<int:pk>/", UpdateBlog.as_view(), name="editblog"),
    path('comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
    path('post_detail/<int:post_id>/', views.post_detail, name='post_detail'),
]