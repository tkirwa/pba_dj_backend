from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from knox import views as knox_views


urlpatterns = [
    path("admin/", admin.site.urls),
    # Include your custom accounts URLs
    path("accounts/", include("accounts.urls")),
    # Include your custom API URLs
    path("api/v1/", include("api.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
