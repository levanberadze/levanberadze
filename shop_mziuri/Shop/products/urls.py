from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    path('create_product/', views.create_product, name='create_product'),
    path('product/<int:id>/update/', views.product_update, name='product_update'),
    path('product/<int:id>/delete/', views.product_delete, name='product_delete')
]


from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)