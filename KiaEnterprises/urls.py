
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter

from inventory.views import ProductViewSet
from inventory.views import CategoryViewSet
import authapp

admin.site.site_header = 'Kia Enterprises'  

router = DefaultRouter()
router.register(r'inventory', viewset=ProductViewSet, basename='ProductQueryset')
router.register(r'category', viewset=CategoryViewSet, basename='CategoryQueryset')

urlpatterns = [
  
  path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
  path('admin/', admin.site.urls),
  path('',include(router.urls)),   
 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)