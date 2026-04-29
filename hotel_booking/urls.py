"""
Root URL configuration for hotel_booking project.
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import render
from django.urls import include, path


def home_page(request):
    """Serve the landing page."""
    return render(request, "pages/index.html")


urlpatterns = [
    # Pages
    path("", home_page, name="home"),

    # Admin
    path("admin/", admin.site.urls),

    # API endpoints
    path("accounts/", include("accounts.urls")),
    path("rooms/", include("rooms.urls")),
    path("bookings/", include("rooms.booking_urls")),
    path("payments/", include("payments.urls")),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
