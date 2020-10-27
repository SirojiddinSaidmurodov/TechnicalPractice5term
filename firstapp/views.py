from django.shortcuts import render

# Create your views here.
from firstapp.models import Post


def post_list(request):
    return render(request, 'firstapp/post_list.html', {})


def about_page(request):
    return render(request, 'firstapp/about.html')


def index(request):
    text = Post.objects.all()
    return render(request, "firstapp/index.html", {"text": text})
