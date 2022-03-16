"""root URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from backend.views import BlogList, ContactView, AboutAsView, IndexView, GalleryView, BlogDetailView, AboutKgView, \
    DirectionView, DirectionDetailView, WDirectionDetailView

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('ckeditor/', include('ckeditor_uploader.urls')),
                  path('blocks/', BlogList.as_view(), name='blocks'),
                  path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
                  path('contact/', ContactView.as_view(), name='contact'),
                  path('about_us/', AboutAsView.as_view(), name='about_us'),
                  path('', IndexView.as_view(), name='index'),
                  path('gallery/', GalleryView.as_view(), name='gallery'),
                  path('about_kg/', AboutKgView.as_view(), name='about_kg'),
                  path('direction/', DirectionView.as_view(), name='direction'),
                  path('direction_w/<int:pk>/', DirectionDetailView.as_view(), name='detail_w'),
                  path('directions/<int:pk>/', WDirectionDetailView.as_view(), name='directions'),
                  path('<str:category>', DirectionView.as_view(), name="category")

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
