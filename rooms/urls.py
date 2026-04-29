"""
URL configuration for the rooms app (search only).
"""

from django.shortcuts import render
from django.urls import path

from . import views

app_name = "rooms"


# Page views
def search_page(request):
    return render(request, "rooms/search.html")


def room_detail_page(request):
    return render(request, "rooms/room_details.html")


urlpatterns = [
    # Pages
    path("search/page/", search_page, name="search-page"),
    path("room/page/", room_detail_page, name="room-detail-page"),

    # API endpoints
    path("search/", views.SearchRoomsView.as_view(), name="search"),
    path("<uuid:room_id>/", views.RoomDetailView.as_view(), name="detail"),
]
