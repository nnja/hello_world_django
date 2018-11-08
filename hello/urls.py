from django.urls import path, re_path

from hello import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:name>', views.index, name='index'),
]