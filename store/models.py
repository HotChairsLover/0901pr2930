from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(blank=True, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.username}"


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название")
    photo = models.ImageField(verbose_name="Фото", upload_to="img/")
    price = models.IntegerField(verbose_name="Цена")

    def __str__(self):
        return f"{self.name}"


class Orders(models.Model):
    client = models.ForeignKey("User", on_delete=models.CASCADE, related_name="orders", verbose_name="Клиент")
    complete_order = models.BooleanField(verbose_name="Выполнен", default=False, null=True)

    def __str__(self):
        return f"{self.client}"


class Cart(models.Model):
    order = models.ForeignKey("Orders", on_delete=models.CASCADE, related_name="cart_orders", verbose_name="Заказ")
    products = models.ManyToManyField("Product", blank=True, related_name="products", verbose_name="Продукты")
    summ = models.IntegerField(blank=True, null=True, verbose_name="Цена заказа")

    def __str__(self):
        return f"{self.id}"


