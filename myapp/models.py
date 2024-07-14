from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Book(models.Model):
    book_name=models.CharField(max_length=100)
    book_price=models.IntegerField()
    year=models.IntegerField()

    def __str__(self):
        return self.book_name
