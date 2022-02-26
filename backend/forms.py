from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget

from backend.models import IndexText


class IndexTextAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = IndexText
        fields = '__all__'


class IndexTextAdmin(admin.ModelAdmin):
    form = IndexTextAdminForm


admin.site.register(IndexText, IndexTextAdmin)
