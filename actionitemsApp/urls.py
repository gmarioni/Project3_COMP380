from django.urls import path
from . import views

urlpatterns = [
    path('',views.main, name="actionitems"),
    path('<int:pk>/',views.item,name="actionitem"),
    path('create', views.create,name="create-actionitem"),
    path('<int:pk>/update',views.update,name="update-actionitem"),
    path('<int:pk>/delete',views.delete,name="delete-actionitem"),
]