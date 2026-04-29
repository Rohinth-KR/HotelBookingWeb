"""
URL configuration for booking endpoints (Phase 3).
"""

from django.shortcuts import render
from django.urls import path

from rooms import views

app_name = "bookings"


# Page views
def my_bookings_page(request):
    return render(request, "bookings/my_bookings.html")


def confirmation_page(request):
    return render(request, "bookings/confirmation.html")


urlpatterns = [
    # Pages
    path("my-bookings/page/", my_bookings_page, name="my-bookings-page"),
    path("confirmation/page/", confirmation_page, name="confirmation-page"),

    # API endpoints
    path("hold/", views.HoldRoomView.as_view(), name="hold"),
    path("<uuid:booking_id>/pay/", views.ProcessPaymentView.as_view(), name="pay"),
    path("<uuid:booking_id>/cancel/", views.CancelBookingView.as_view(), name="cancel"),
    path("<uuid:booking_id>/", views.BookingDetailView.as_view(), name="detail"),
    path("ref/<str:booking_ref>/confirmation/", views.ConfirmationView.as_view(), name="confirmation"),
    path("my/", views.MyBookingsView.as_view(), name="my-bookings"),
]
