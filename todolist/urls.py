from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('update/<str:pk>/', views.updatelist, name="update"),
    path('delete/<str:pk>/', views.deleteTodo, name="delete"),
 
]