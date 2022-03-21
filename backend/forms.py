from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget

from backend.models import IndexText, DropAs


class IndexTextAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = IndexText
        fields = '__all__'


class IndexTextAdmin(admin.ModelAdmin):
    form = IndexTextAdminForm


admin.site.register(IndexText, IndexTextAdmin)


class DropAsForm(forms.ModelForm):
    class Meta:
        model = DropAs
        fields = '__all__'


