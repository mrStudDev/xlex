from pyexpat import model
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import PostsXlex, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy


class PostsListView(ListView):
    model = PostsXlex
    template_name = 'templates_posts/posts_list.html'
    ordering = ['-data']


class PostsSingleView(DetailView):
    model = PostsXlex
    template_name = 'templates_posts/post_single.html'


def CategoryView(request, cats):
    category_posts = PostsXlex.objects.filter(category=cats)
    return render(request, 'templates_posts/categories.html', {'cats': cats.title(), 'category_posts': category_posts})


class AddPostView(CreateView):
    model = PostsXlex
    form_class = PostForm
    template_name = 'templates_posts/add_post.html'


class AddCategoryView(CreateView):
    model = Category
    form_class = PostForm
    template_name = 'templates_posts/add_category.html'
    fields = '__all__'


class UpdatePostView(UpdateView):
    model = PostsXlex
    form_class = EditForm
    template_name = 'templates_posts/update_post.html'
    success_url = reverse_lazy('home')


class DeletePostView(DeleteView):
    model = PostsXlex
    template_name = 'templates_posts/delete_post.html'
    success_url = reverse_lazy('home')
