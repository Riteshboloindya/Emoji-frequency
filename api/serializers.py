from rest_framework import serializers
from .models import Student,Comment

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model=Student
        fields ='__all__'



    """ name= serializers.CharField(max_length=100)
    roll= serializers.IntegerField()
    city= serializers.CharField(max_length=100)  """ 

class CommentSerializer(serializers.ModelSerializer):
    class Meta: 
        model=Comment
        fields='__all__'

