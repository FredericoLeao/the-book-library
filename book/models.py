from django.db import models
from book.model_base import TimeStampedModel


class Author(TimeStampedModel):
    name = models.CharField(max_length=200)
    description = models.TextField()


class Category(TimeStampedModel):
    name = models.CharField(max_length=200)
    parent = models.IntegerField(default=0)
    description = models.TextField()


class Book(TimeStampedModel):
    original_name = models.CharField(max_length=300)
    edition_name = models.CharField(max_length=300)
    description = models.TextField()
    author = models.ManyToManyField(Author)
    category = models.ManyToManyField(Category)

