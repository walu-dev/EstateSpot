from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static 
from django.urls import path
from properties.views import  property_list, property_retrieve, property_create, property_update, property_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', property_list),
    path('properties/<pk>/', property_retrieve),
    path('add-property/', property_create),
    path('properties/<pk>/edit/', property_update),
    path('properties/<pk>/delete/', property_delete)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)