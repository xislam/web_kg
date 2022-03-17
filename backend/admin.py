from django.contrib import admin

from backend.models import IndexText, IndexSlider1, Direction,\
    CategoryDirection, Contact, Blog, Gallery, AboutUs, Links, AboutKg

admin.site.register(IndexText)
admin.site.register(IndexSlider1)
admin.site.register(Direction)
admin.site.register(CategoryDirection)
admin.site.register(Contact)
admin.site.register(Blog)
admin.site.register(Gallery)
admin.site.register(AboutUs)
admin.site.register(AboutKg)
admin.site.register(Links)
admin.site.site_header = 'KYRGYZ LAND  ADMIN'
