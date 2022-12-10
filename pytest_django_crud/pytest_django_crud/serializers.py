from rest_framework import serializers  
from .models import students  
  
class StudentSerializer(serializers.ModelSerializer):  
    first_name = serializers.CharField(max_length=200, required=True)  
    last_name = serializers.CharField(max_length=200, required=True)  
    address = serializers.CharField(max_length=200, required=True)  
    roll_number = serializers.IntegerField()  
    mobile = serializers.CharField(max_length=10, required=True)  
  
    class Meta:  
        model = students  
        fields = ('__all__')  