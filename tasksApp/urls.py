from django.urls import path
from . import views

urlpatterns = [
    path('',views.main, name="tasks"),
    path('<int:pk>/',views.item,name="task"),
    path('create', views.create,name="create-task"),
    path('<int:pk>/update',views.update,name="update-task"),
    path('<int:pk>/delete',views.delete,name="delete-task"),
]