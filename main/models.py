from django.db import models


class Item(models.Model):
    slug = models.SlugField('Unique name', unique=True)
    title = models.CharField('Name of the item', max_length=200)
    image = models.CharField('Image', max_length=50)
    desc = models.TextField('Item description')
    price = models.DecimalField('Item price', max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title


class Order(models.Model):
    name = models.CharField('Name: ', max_length=200)
    surname = models.CharField('Surname: ', max_length=200)
    phone = models.CharField('Phone: ', max_length=200)
    email = models.CharField('Email: ', max_length=200)
    basket = models.TextField('Items: ')

    def __str__(self):
        return self.name + ' ' + self.surname + ' (' + self.phone + ')'
