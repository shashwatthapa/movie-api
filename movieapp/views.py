from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserRegistrationSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

class UserRegistrationView(APIView):
    def post(self,request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message":"User created successfully"
            },status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
class UserLoginView(APIView):
    def post(self,request):
        user = authenticate(username=request.data['username'],password=request.data['password'])
        if user:
            token,created = Token.objects.get_or_create(user=user)
            return Response({'token':token.key})
        else:
            return Response({'error':'Invalid credentials'})

class LogoutView(APIView):
    def post(self,request):
        permission_classes = [IsAuthenticated]
        request.user.auth_token.delete()
        return Response({'message':'Logged out successfully'})