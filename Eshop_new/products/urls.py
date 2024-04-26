from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .import views


urlpatterns = [
    path('',views.home,name='home'),
    path('products',views.list_products,name='product_list'),
    path('product/<pk>',views.product_detail,name='detail_product'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)