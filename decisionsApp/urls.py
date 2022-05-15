from django.urls import path
from . import views

urlpatterns = [
    path('',views.main, name="decisions"),
    path('<int:pk>/',views.item,name="decision"),
    path('create', views.create,name="create-decision"),
    path('<int:pk>/update',views.update,name="update-decision"),
    path('<int:pk>/delete',views.delete,name="delete-decision"),
]