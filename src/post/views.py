from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseNotFound
from .models import Post
from django.views.generic import DeleteView
from rest_framework import generics
from .serializers import PostSerializer
from .permissions import IsOwnerOrReadOnly
from django.contrib.auth.decorators import login_required
from .forms import MyForm

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]

class PostCreate(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('post:home')  
    template_name = 'post/post_confirm_delete.html'

def home_view(request):
    return render(request, 'home.html')

def posts(request):
    return HttpResponse('<h1>All posts:</h1>')

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post/post_detail.html', {'post': post})

def post_archive(request, year):
    if int(year) > 2024 or int(year) < 1995:
        raise Http404
    return HttpResponse(f'archive for {year}')

def get_post_handler(request):
    if request.POST:
        return HttpResponse('POST request')
    return HttpResponse('GET request')

def page_404(request, exception):
    return HttpResponseNotFound("<h3>Page not found :^(</h3>")

def home_view(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})

@login_required
def post_list(request):
    posts = Post.objects.all() 
    return render(request, 'post/post_list.html', {'posts': posts})

def my_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            return HttpResponse("Form submitted successfully!") 
    else:
        form = MyForm()
    return render(request, 'my_template.html', {'form': form})
