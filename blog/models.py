from django.db import models


class Article(models.Model):
    title = models.CharField(
        max_length=255,
    )
    text = models.CharField(
        max_length=1000,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    category = models.ForeignKey(
        'Category', 
        on_delete=models.SET_NULL,
        null=True,
    )
    
    def __str__(self):
        return f'Статья: \'{self.title}\''


class Category(models.Model):
    name = models.CharField(
        max_length=255,
    )
    
    def __str__(self):
        return f': \'{self.name}\''
