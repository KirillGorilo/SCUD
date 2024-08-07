from users.models import User
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'], 
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            middle_name=validated_data['middle_name'],
            email=validated_data['email'],
            description=validated_data['description'],
            id=validated_data['id'],
        )

    class Meta:
        model = User
        fields = ["id", 'username', 'password', 'first_name', 'last_name', 'email', 'identity_qrcode', "middle_name", 'description']



class UserRegisterSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(required=True)

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Такой email уже занят.")
        return value

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'], 
            password=validated_data['password'],
            email=validated_data['email'],
        )
        return user

    class Meta:
        model = User
        fields = ['username', 'email', "password"]


class AuthCustomTokenSerializer(serializers.Serializer):
    login = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        login = data.get('login')
        password = data.get('password')

        if login and password:
            user = authenticate(username=login, password=password)
            if user:
                if user.is_active:
                    data['user'] = user
                else:
                    raise serializers.ValidationError("User is disabled.")
            else:
                raise serializers.ValidationError("Unable to log in with provided credentials.")
        else:
            raise serializers.ValidationError("Must include 'login' and 'password'")
        
        return data


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        
        data.update({
            'login': self.user.username,
            'firstName': self.user.first_name,
            'lastName': self.user.last_name,
            'middleName': self.user.middle_name,
            'email': self.user.email,
            'qrcode': self.user.identity_qrcode,
            'id': self.user.id
        })
        
        return data