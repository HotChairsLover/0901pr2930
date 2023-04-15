from django.urls import path
from . import views

urlpatterns = [
    path("items", views.ItemsView.as_view(), name="store_items"),
    path("cart", views.CartView.as_view(), name="store_cart"),
    path("orders", views.OrdersView.as_view(), name="store_orders"),
]
