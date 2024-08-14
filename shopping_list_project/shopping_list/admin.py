# shopping_list/admin.py

from django.contrib import admin
from shopping_list_project.shopping_list.models import Item

admin.site.register(Item)
