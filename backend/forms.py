from django import forms

from backend.models import DropAs


class DropAsForm(forms.ModelForm):
    class Meta:
        model = DropAs
        fields = '__all__'
