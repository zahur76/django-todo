from django import forms
# Import database we are storing infomation
# We need  to know what database to populate
from .models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'done']
