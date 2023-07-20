from django.urls import path

from app_blog.views import PostListView, PostDeleteView, PostCreateView, PostDetailView, PostUpdateView

urlpatterns = [
    path('', PostListView.as_view(), name='all_posts'),
    path('<slug:slug>', PostDetailView.as_view(), name='post_details'),
    path('create_post/', PostCreateView.as_view(), name='post_create'),
    path('edit_post/<slug:slug>', PostUpdateView.as_view(), name='post_edit'),
    path('delete_post/<slug:slug>', PostDeleteView.as_view(), name='post_delete')
]