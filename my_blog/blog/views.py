from django.shortcuts import render
from django.http import  HttpResponse
from .models import Post
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
# Create your views here.
context={
    'posts':Post.objects.all()
}
def home(request):
    return render(request,'blog/Home.html',context)
def about(request):
    return render(request,'blog/About.html')

class PostList(ListView):
    model=Post
    context_object_name ='posts'
    template_name ='blog/post_list.html'
    ordering = ['-datePosted']
    paginate_by = 10
class PostDetailView(DetailView):
    model=Post
class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        else:
            return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
        model = Post
        success_url = "/"

        def test_func(self):
            post = self.get_object()
            if self.request.user == post.author:
                return True
            else:
                return False
