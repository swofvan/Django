from django.urls import path
from . import views

appname = 'teachers'

urlpatterns = [
    path ('', views.teacher, name='teacherslist'),
    path ('addteacher/', views.addteacher, name='addteachers')
]