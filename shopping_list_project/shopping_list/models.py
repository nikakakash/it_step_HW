

from django.db import models

class Item(models.Model):
    item_name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    purchased = models.BooleanField(default=False)

    def __str__(self):
        return self.item_name
