"""
URL configuration for payment endpoints.
"""

from django.shortcuts import render
from django.urls import path

from . import views

app_name = "payments"


# Page views
def checkout_page(request):
    return render(request, "payments/checkout.html")


urlpatterns = [
    # Pages
    path("checkout/page/", checkout_page, name="checkout-page"),

    # API endpoints
    path("create-order/", views.CreateOrderView.as_view(), name="create-order"),
    path("verify/", views.VerifyPaymentView.as_view(), name="verify"),
    path("webhook/", views.WebhookView.as_view(), name="webhook"),
]
