from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from .models import Post

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, './templates/post_detail.html', {'post': post})
def home_view(request):
    return render(request, 'home.html')

def posts(request):
    return HttpResponse('<h1>All posts:</h1>')

def post_detail(request, post_id):
    return HttpResponse(f'detail: {post_id}')

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
