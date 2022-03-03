from django.shortcuts import render
from django.views.generic import ListView

from backend.models import Blog


class BlogList(ListView):
    template_name = 'blog.html'
    model = Blog
    context_object_name = 'blocks'
