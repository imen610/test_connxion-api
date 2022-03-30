
from django.urls import path, re_path
from .views import ListTodo, detailTodo 

 
urlpatterns = [
    path('list/',ListTodo.as_view(),name="todos"),
    path('<int:pk>/',detailTodo.as_view(),name="todos")
     
 ]