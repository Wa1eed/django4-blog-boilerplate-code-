from django.urls import path
from .views import PostListView, CreatePostView, PostDeatiledView

urlpatterns = [
    
    path('', PostListView.as_view(), name='posts'),
    path('create/', CreatePostView.as_view(), name='create'),
    path('post/<int:pk>', PostDeatiledView.as_view(), name='view'),
]
