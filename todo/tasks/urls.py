from django.contrib import admin
from django.urls import path , include
from tasks import views

urlpatterns = [
    path('', views.index , name = 'list'),
    path('edit/<str:pk>/', views.Edit , name  = 'edit'),
    path('delete/<str:pk>/', views.deletetask, name  = 'delete')


]
