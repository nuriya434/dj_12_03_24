from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseNotFound
from .models import Post
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    success_url = reverse_lazy('home')

    def delete(self, request, *args, **kwargs):
        print("Deleting post...")
        self.object = self.get_object()
        success_url = self.get_success_url()
        print(f"Post ID before deletion: {self.object.id}")
        self.object.delete()
        print(f"Post ID after deletion: {self.object.id}")
        return redirect(success_url)

    def get(self, request, *args, **kwargs):
        post = self.get_object()
        return render(request, 'post_detail.html', {'post': post})

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
