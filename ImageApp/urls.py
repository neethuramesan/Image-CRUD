from django.urls import path,include
from .import views
urlpatterns = [
    path('',views.load,name="load"),
    path('add_user',views.add_user,name="add_user"),
    path('show',views.show,name="show"),
    path('edit/<int:pk>',views.edit,name="edit"),
    path('delete/<int:pk>',views.delete,name="delete"),
    
    
]
