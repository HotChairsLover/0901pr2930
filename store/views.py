from django.shortcuts import render
from django.views import View, generic
from django.views.generic.edit import ModelFormMixin

from . import models
from . import forms


class CartView(generic.ListView):
    model = models.Cart
    template_name = "store/cart.html"
    context_object_name = "carts"

    def post(self, request, *args, **kwargs):
        order_id = request.POST.get("order_id")
        user_id = request.user.id
        order = models.Orders.objects.filter(id=order_id, client_id=user_id)
        if order.count() == 1:
            order = order.get()
            order.complete_order = True
            order.save()
        return self.get(request)
    

class ItemsView(generic.ListView):
    model = models.Product
    template_name = "store/items.html"
    context_object_name = "items"

    def post(self, request, *args, **kwargs):
        product_id = request.POST.get("item_id")
        product = models.Product.objects.filter(id=product_id).get()
        user_id = request.user.id
        incomplete_orders = models.Orders.objects.filter(client_id=user_id, complete_order=False)
        if incomplete_orders.count() == 0:
            order = models.Orders.objects.create(client_id=user_id)
            order.save()
            cart = models.Cart.objects.create(order_id=order.id)
            product_to_cart = models.ToCart(product=product, product_cart=cart)
            product_to_cart.save()
            cart.summ = product.price
            cart.save()
        else:
            cart = models.Cart.objects.filter(order_id=incomplete_orders.get().id).get()
            product_to_cart = models.ToCart(product=product, product_cart=cart)
            product_to_cart.save()
            cart.summ += product.price
            cart.save()
        return self.get(request)



