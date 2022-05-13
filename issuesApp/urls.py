from django.urls import path
from . import views

urlpatterns = [
    path('',views.main, name="issues"),
    path('<int:pk>/',views.item,name="issue"),
    path('create', views.create,name="create-issue"),
    path('<int:pk>/update',views.update,name="update-issue"),
    path('<int:pk>/delete',views.delete,name="delete-issue"),
]