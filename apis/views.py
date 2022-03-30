from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from todos import models
from .serializers import todoSerilazer

class ListTodo(generics.ListCreateAPIView):
    queryset=models.Todo.objects.all()
    serializer_class=todoSerilazer
class detailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.Todo.objects.all()
    serializer_class=todoSerilazer
 
