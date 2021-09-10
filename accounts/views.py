from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework.authtoken.models import Token

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
