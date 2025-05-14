from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,viewsets
from .serializers import UserRegistrationSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from .serializers import MovieSerializer
from .models import Movies

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
    permission_classes = [IsAuthenticated]
    def post(self,request):
        request.user.auth_token.delete()
        return Response({'message':'Logged out successfully'})
    
class MovieViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer
