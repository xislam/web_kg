from django.shortcuts import render
from django.views.generic import ListView, DetailView

from backend.models import Blog, Contact, AboutUs, Gallery, Links, IndexText, AboutKg, Direction, IndexSlider1, \
    CategoryDirection


class BlogList(ListView):
    template_name = 'blog.html'
    model = Blog
    paginate_by = 3
    context_object_name = 'blocks'

    def get_context_data(self, **kwargs):
        context = super(BlogList, self).get_context_data(**kwargs)
        context["contact"] = Contact.objects.all()
        context["links"] = Links.objects.first()
        return context


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog_ditail.html'
    context_object_name = 'blog'

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        context["links"] = Links.objects.first()
        return context


class ContactView(ListView):
    template_name = 'contact.html'
    model = Contact
    context_object_name = 'contact'

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context["contacts"] = Contact.objects.first()
        context["links"] = Links.objects.first()
        return context


class AboutAsView(ListView):
    template_name = 'about_us.html'
    model = AboutUs
    context_object_name = 'about_us'

    def get_context_data(self, **kwargs):
        context = super(AboutAsView, self).get_context_data(**kwargs)
        context["sliders"] = Gallery.objects.all()
        context["contact"] = Contact.objects.all()
        context["links"] = Links.objects.first()
        return context


class AboutKgView(ListView):
    template_name = 'about_kg.html'
    model = AboutKg
    context_object_name = 'about_kg'

    def get_context_data(self, **kwargs):
        context = super(AboutKgView, self).get_context_data(**kwargs)
        context["sliders"] = Gallery.objects.all()
        context["contact"] = Contact.objects.all()
        context["links"] = Links.objects.first()
        return context


class IndexView(ListView):
    template_name = 'mainTwo.html'
    model = IndexText
    context_object_name = 'index'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['slider1'] = IndexSlider1.objects.all()
        context['birection'] = Direction.objects.all()
        context['contact'] = Contact.objects.all()
        return context


class GalleryView(ListView):
    template_name = 'gallery.html'
    model = Gallery
    context_object_name = "gallery"

    def get_context_data(self, **kwargs):
        context = super(GalleryView, self).get_context_data(**kwargs)
        context['contact'] = Contact.objects.all()
        return context


class DirectionView(ListView):
    template_name = 'destinations.html'
    model = Direction
    context_object_name = 'direction'

    def get_context_data(self, **kwargs):
        context = super(DirectionView, self).get_context_data(**kwargs)
        context['slider1'] = IndexSlider1.objects.all()
        context['contact'] = Contact.objects.all()
        context["categories"] = CategoryDirection.objects.all()
        context["directions"] = Direction.objects.all()
        category = self.kwargs.get('category')

        if category:
            context["directions"] = Direction.objects.filter(category__name=category)
        if category == "ALL":
            context["directions"] = Direction.objects.all()

        return context


class DirectionDetailView(DetailView):
    model = IndexSlider1
    template_name = 'parts_description.html'
    context_object_name = 'parts'

    def get_context_data(self, **kwargs):
        context = super(DirectionDetailView, self).get_context_data(**kwargs)
        context["links"] = Links.objects.first()
        context["contact"] = Contact.objects.all()
        return context


class WDirectionDetailView(DetailView):
    model = Direction
    template_name = 'directions_ditaile.html'
    context_object_name = 'directions'

    def get_context_data(self, **kwargs):
        context = super(WDirectionDetailView, self).get_context_data(**kwargs)
        context["links"] = Links.objects.first()
        context["contact"] = Contact.objects.all()
        return context
