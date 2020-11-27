from django import forms
# Import database we are storing information
# We need  to know what fields are required in form
from .models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'done']
