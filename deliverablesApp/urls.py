from django.urls import path
from . import views

urlpatterns = [
    path('',views.main, name="deliverables"),
    path('<int:pk>/',views.item,name="deliverable"),
    path('create', views.create,name="create-deliverable"),
    path('<int:pk>/update',views.update,name="update-deliverable"),
    path('<int:pk>/delete',views.delete,name="delete-deliverable"),
]