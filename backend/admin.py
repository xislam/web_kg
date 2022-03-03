from django.contrib import admin

from backend.models import IndexText, IndexSlider1, Direction, CategoryDirection, Contacts, Blog

admin.site.register(IndexText)
admin.site.register(IndexSlider1)
admin.site.register(Direction)
admin.site.register(CategoryDirection)
admin.site.register(Contacts)
admin.site.register(Blog)