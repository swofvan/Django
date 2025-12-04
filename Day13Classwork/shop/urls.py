from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_product, name='create'),
    path('list/', views.list_product, name = 'list'),
    path('<int:pk>/update/', views.update_product, name = 'update'),
    path('<int:pk>/delete/', views.delete_product, name = 'delete'),
]