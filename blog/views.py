from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import PostSerializer

from .models import Post
from django.views.generic import (ListView,
                                    DetailView,
                                    CreateView,
                                    UpdateView,
                                    DeleteView,
                                  )
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin




# def home(request):
#     content={
#
#         'posts':Post.objects.order_by('-date_posted'),
#     }
#     return render(request,'blog/home.html',content)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # default: app/model_list.html
    context_object_name = 'posts'   #default: object_list
    ordering = ['-date_posted']
    paginate_by=5

class UserPostsView(ListView):
     # model = Post
    template_name = 'blog/user_posts.html' # default: app/model_list.html
    context_object_name = 'posts'   #default: object_list
    # ordering = ['-date_posted']
    paginate_by=5

    def get_queryset(self):
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post

class PostCtreateView(LoginRequiredMixin,CreateView):
    model=Post
    #context_object_name='post'
    #template_name = 'blog/post_form.html'
    fields=['title','content']


    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Post
    fields=['title','content']

    #this view uses 'post_form.html'

    # def form_valid(self, form):
    #     form.instance.author=self.request.user
    #     return super().form_valid(form)

    def test_func(self):
        post=self.get_object()
        if self.request.user == post.author :
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post
    template_name = 'blog/delete.html'
    # success_url='/'
    success_url = reverse_lazy('blog-home')
    def test_func(self):
        post=self.get_object()
        if self.request.user == post.author :
            return True
        return False

def about(request):
    return render(request,'about.html',{'title':'About'})

class PostList(APIView):

    def get(self,request):
        posts=Post.objects.all()
        serializer=PostSerializer(posts,many=True)
        return Response(serializer.data)

    def post(self):
        pass
