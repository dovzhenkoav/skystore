from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from pytils.translit import slugify
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from app_blog.models import BlogPost
# from app_blog.forms import BlogPostForm

# Create your views here.


class PostListView(ListView):
    model = BlogPost
    template_name = 'blog/index.html'

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class PostDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/post_details.html'
    context_object_name = "post"

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object


class PostCreateView(CreateView):
    model = BlogPost
    fields = ('name', 'description', 'image',)
    success_url = reverse_lazy('all_posts')
    template_name = 'blog/post_create.html'

    def form_valid(self, form):
        if form.is_valid():
            new_form = form.save()
            new_form.slug = slugify(new_form.name)
            new_form.save()
        return super().form_valid(form)


class PostUpdateView(UpdateView):
    model = BlogPost
    fields = ('name', 'description', 'image',)
    template_name = 'blog/post_create.html'

    def form_valid(self, form):
        if form.is_valid():
            new_form = form.save()
            new_form.slug = slugify(new_form.name)
            new_form.save()
            self.kwargs['slug'] = new_form.slug
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post_details', args=(self.kwargs.get('slug'),))


class PostDeleteView(DeleteView):
    model = BlogPost
    success_url = reverse_lazy('all_posts')
    template_name = 'blog/post_delete_confirmation.html'

