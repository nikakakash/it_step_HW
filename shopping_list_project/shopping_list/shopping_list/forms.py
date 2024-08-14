# shopping_list/forms.py

from django import forms
from shopping_list_project.shopping_list.models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['item_name', 'quantity']
