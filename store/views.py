from django.shortcuts import render
from django.views import View, generic
from django.views.generic.edit import ModelFormMixin

from . import models
from . import forms


class OrdersView(generic.ListView):
    model = models.Cart
    template_name = "store/orders.html"
    context_object_name = "carts"

class CartView(generic.ListView):
    model = models.Cart
    template_name = "store/cart.html"
    context_object_name = "carts"

    def post(self, request, *args, **kwargs):
        user_id = request.user.id
        order_id = request.POST.get("order_id")
        if order_id:
            return self.post_complete_order(order_id, request, user_id)
        product_id = request.POST.get("product_id")
        if product_id:
            return self.post_remove_from_cart(product_id, request, user_id)
        return self.get(request)

    def post_remove_from_cart(self, product_id, request, user_id):
        cart_id = request.POST.get("cart_id")
        product = models.Product.objects.filter(id=product_id)
        cart = models.Cart.objects.filter(id=cart_id, order__client_id=user_id)
        if cart.count() == 1 and product.count() == 1:
            product = product.get()
            cart = cart.get()
            cart.summ -= product.price
            product_through = models.ToCart.objects.filter(product_id=product_id, product_cart_id=cart_id).first()
            product_through.delete()
            cart.save()
        return self.get(request)

    def post_complete_order(self, order_id, request, user_id):
        order = models.Orders.objects.filter(id=order_id, client_id=user_id)
        if order.count() == 1:
            order = order.get()
            order.post_complete_order = True
            order.save()
        return self.get(request)


class ItemsView(generic.ListView):
    model = models.Product
    template_name = "store/items.html"
    context_object_name = "items"

    def post(self, request, *args, **kwargs):
        product_id = request.POST.get("item_id")
        if product_id:
            return self.post_add_to_cart(product_id, request)
        return self.get(request)

    def post_add_to_cart(self, product_id, request):
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



