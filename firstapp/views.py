from django.shortcuts import render, redirect
# Create your views here.
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import DeleteView, UpdateView, CreateView

from firstapp.forms import PostForm
from firstapp.models import Post


def post_list(request):
    return render(request, 'firstapp/post_list.html', {})


def about_page(request):
    return render(request, 'firstapp/about.html')


def index(request):
    query = request.GET.get("search")
    if query:
        text = Post.objects.filter(title__contains=query)
    else:
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


class PostDetailView(generic.DetailView):
    model = Post
    slug_field = 'id'


class PostCreate(CreateView):
    model = Post
    fields = ('author', 'title', 'text', 'created_date', 'publish_date')


class PostUpdate(UpdateView):
    model = Post
    fields = ('author', 'title', 'text', 'created_date', 'publish_date')


class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('index_list')
