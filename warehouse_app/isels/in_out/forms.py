from django import forms  
from .models import part_form

class parts_form(forms.ModelForm):
    class Meta:
        model = part_form
        fields = "__all__"