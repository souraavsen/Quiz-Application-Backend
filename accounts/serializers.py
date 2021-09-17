from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(allow_blank=False, max_length=300)
    last_name = serializers.CharField(max_length=300)
    email = serializers.EmailField(allow_blank=False, max_length=300)
    image = serializers.ImageField(max_length=None, allow_empty_file=False)
    class Meta:
        model = User
        fields = ('username', 'email', "image", 'password', 'first_name', 'last_name')

    def validate(self,attrs):
        email = attrs.get('email', '')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': ('Email is already exist')})
        else:
            return super().validate(attrs)

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
        

class UserOperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')
        extra_kwargs = {'email': {'required': False}, 'username':{'required':False}}


