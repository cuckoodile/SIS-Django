from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework import serializers

from django.contrib.auth.models import User

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['email'] = user.email
        # ...

        return token
    
class UsersSerializer(serializers.ModelSerializer):
    password_confirmation = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'email',  'password', 'password_confirmation')
        extra_kwargs = {
            'password': {'write_only': True},
        }
    
    # Create user using POST method
    def create(self, validated_data):
        if validated_data['password'] != validated_data['password_confirmation']:
            raise serializers.ValidationError('Password and Password Confirmation does not match.')
        validated_data.pop('password_confirmation')
        return super().create(validated_data)