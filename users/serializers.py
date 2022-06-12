from rest_framework import serializers
from .models import User

class UserRegistrationSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email','user_type','password', 'password2',]
        extra_kwargs = {
            'password': {
                'write_only':True
            }
        }

    def save(self, request):
        user = User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            user_type=self.validated_data['user_type'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password':'Passwords must match.'})
        user.set_password(password)
        user.save()
        return user