from django.shortcuts import render, redirect

# Create your views here.
from firstapp.forms import PostForm
from firstapp.models import Post


def post_list(request):
    return render(request, 'firstapp/post_list.html', {})


def about_page(request):
    return render(request, 'firstapp/about.html')


def index(request):
    text = Post.objects.all()
    return render(request, "firstapp/index.html", {"text": text})


def post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'firstapp/post_form.html', {'form': form})


def filter_list(request):
    query = request.GET.get("search")
    text = Post.objects.filter(title__contains=query)
    return render(request, "firstapp/index.html", {"text": text})
