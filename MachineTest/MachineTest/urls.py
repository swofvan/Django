"""
URL configuration for MachineTest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from bookmark import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.signup, name = 'signup'),
    path ('login/', views.login_page, name='login'),
    path('add_bookmarks/', views.add_bookmarks, name = 'add_bookmarks'),
    path('list_bookmarks/', views.list_bookmarks, name='list_bookmarks'),
    path('edit/<int:id>/', views.edit_bookmark, name='edit'),
    path('delete/<int:pk>/', views.dlt_bookmark, name='delete'),
    path('logout/', views.logout_page, name='logout')
]
