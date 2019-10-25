from django.db import models
from django.urls import reverse
from datetime import date


# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    desc = models.TextField(max_length=300)
    image = models.ImageField(upload_to='products', default="")
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:productView', args=[self.id])


class Women(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    desc = models.TextField(max_length=300)
    image = models.ImageField(upload_to='products', default="")
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:womenView', args=[self.id])


class Men(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    desc = models.TextField(max_length=300)
    image = models.ImageField(upload_to='products', default="")
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:menView', args=[self.id])


class Blog(models.Model):
    image = models.ImageField(upload_to='products', default="")
    title = models.CharField('post title', max_length=200)
    description = models.TextField()
    posted_date = models.DateField(default=date.today)

    def __str__(self):
        return self.title


class Comment(models.Model):
    message = models.TextField('Message')
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    date_comment = models.DateField(default=date.today)
    post_id = models.ForeignKey(Blog, on_delete=models.CASCADE)
