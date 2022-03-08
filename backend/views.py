from django.shortcuts import render
from django.views.generic import ListView

from backend.models import Blog, Contact, AboutUs, Gallery, Links, IndexText


class BlogList(ListView):
    template_name = 'blog.html'
    model = Blog
    context_object_name = 'blocks'


class ContactView(ListView):
    template_name = 'contact.html'
    model = Contact
    context_object_name = 'contacts'


class AboutAsView(ListView):
    template_name = 'about_us.html'
    model = AboutUs
    context_object_name = 'about_us'

    def get_context_data(self, **kwargs):
        context = super(AboutAsView, self).get_context_data(**kwargs)
        context["sliders"] = Gallery.objects.all()
        context["contacts"] = Contact.objects.first()
        context["links"] = Links.objects.first()
        return context


class IndexView(ListView):
    template_name = 'mainTwo.html'
    model = IndexText
    context_object_name = 'index_text'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context


class GalleryView(ListView):
    template_name = 'gallery.html'
    model = Gallery
    context_object_name = "gallery"

    def get_context_data(self, **kwargs):
        context = super(GalleryView, self).get_context_data(**kwargs)
        return context
