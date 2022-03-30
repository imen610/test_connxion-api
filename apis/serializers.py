from dataclasses import fields
from pyexpat import model
from rest_framework import serializers 
from todos.models import Todo
class todoSerilazer(serializers.ModelSerializer):
    class Meta:
        fields=('id','title','description')
        model= Todo