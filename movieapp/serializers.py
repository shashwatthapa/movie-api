from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Movies,Carts

class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model = User 
        fields= ['username','email','password','password2']
    
    def validate(self,attrs):
        if attrs['password']!=attrs['password2']:
            raise serializers.ValidationError({"password":"Password fields doesnt match"})
        return attrs
        
    def create(self,validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user 

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = '__all__'

class CartsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carts
        fields = ['item','quantity']