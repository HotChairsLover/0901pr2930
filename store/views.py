from django.shortcuts import render
from django.views import View, generic
from django.views.generic.edit import ModelFormMixin

from . import models
from . import forms


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
            cart.products.add(product)
            cart.summ = product.price
            cart.save()
        else:
            cart = models.Cart.objects.filter(order_id=incomplete_orders.get().id).get()
            cart.products.add(product)
            cart.summ += product.price
            cart.save()
        return self.get(request)



