from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # the default path for the admin site
    path('admin/', admin.site.urls),
    path('', include('weather.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
