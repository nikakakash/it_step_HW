# shopping_list/views.py

from django.shortcuts import render, redirect
from models import Item
from shopping_list_project.shopping_list.shopping_list.forms import ItemForm

def index(request):
    items = Item.objects.all()
    return render(request, 'shopping_list/index.html', {'items': items})

def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ItemForm()
    return render(request, 'shopping_list/add_item.html', {'form': form})

def mark_purchased(request, item_id):
    item = Item.objects.get(id=item_id)
    item.purchased = True
    item.save()
    return redirect('index')

def delete_item(request, item_id):
    item = Item.objects.get(id=item_id)
    item.delete()
    return redirect('index')
