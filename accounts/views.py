from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import UserSerializer, UserOperationSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated

class Reistration(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        data={}
        if serializer.is_valid():
            users = serializer.save()
            data['username'] = users.username
            data['email'] = users.email
            data['name']=users.first_name +' '+ users.last_name
            token=Token.objects.get(user=users).key
            data['token']=token
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
""" 
For Test:
{
"first_name": "easrfan",
"last_name":"A",
"username":"aaa",
"password": "123456789",
"email": "asadrfan@example.com"
} 

"""

class UserOperation(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, username, format=None):

        if (User.objects.filter(username=username)):
            user = User.objects.get(username=username)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        return Response([],status=status.HTTP_404_NOT_FOUND)


    def put(self, request, username, format=None):
        current_user = User.objects.get(username=username)
        
        request.data['email'] = current_user.email
        request.data['password'] = make_password(request.data['password'])

        serializer = UserOperationSerializer(current_user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, username, format=None):
        current_user = User.objects.get(username=username)
        current_user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

""" 
{
    "username": "rahul",
    "email": "rahul@example.com",
    "password": "ssg12345",
    "first_name": "Rahul Sen",
    "last_name": "Gupta"
} 
"""