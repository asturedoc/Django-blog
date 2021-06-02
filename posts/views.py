from django.db.models.base import Model
from django.shortcuts import render, get_object_or_404
from .models import Post
#from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ( 
    ListView,
   DetailView,
   CreateView,
   UpdateView,
   DeleteView
   )
# posts = [
#     {
#         'author':'Branda',
#         'title':'introduction to Django',
#         'content':'template inheritance',
#         'date_posted':'August 28, 2021'
#     },
#     {
#         'author':'Brex',
#         'title':'introduction to Flutter',
#         'content':'make your first app ',
#         'date_posted':'May 29, 2021'
#     },

# ]
@login_required
def index(request):
    user = request.user
    if user.is_superuser==True:
        context = {
        'posts':Post.objects.all()
    }
    else:
        context = {
        'posts':user.post_set.all()
    }

    
    
    return render(request, 'posts/home.html', context)

class PostListView(LoginRequiredMixin,ListView):
    model=Post
    template_name='posts/home.html'
    context_object_name='posts'
    ordering=['-date_posted']
    paginate_by=3

class UserPostListView(LoginRequiredMixin,ListView):
    model=Post
    template_name='posts/user_posts.html'
    context_object_name='posts'
    paginate_by=3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')



class PostDetailView(DetailView):
    model=Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model=Post
    fields=['title','content']
    
    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model=Post
    fields=['title','content']
    
    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user==post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model=Post
    success_url='/'

    def test_func(self):
        post = self.get_object()
        if self.request.user==post.author:
            return True
        return False


def about(request):
     return render(request, 'posts/about.html')
