from .models import Post 
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import Postform
# Create your views here.

class PostListView(ListView):
    model = Post
    queryset = Post.objects.all()
    template_name = 'index.html'
    context_object_name = 'posts'
    
class CreatePostView(CreateView):
    Model = Post
    queryset = Post.objects.all()
    template_name = 'create-post.html'
    success_url = reverse_lazy('posts')
    form_class = Postform
    
    
class PostDeatiledView(DetailView):
    Model = Post
    queryset = Post.objects.all()
    template_name = 'view-post.html'
    success_url = reverse_lazy('posts')
       