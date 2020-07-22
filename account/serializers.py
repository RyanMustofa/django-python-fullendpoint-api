from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class AccountCreateSerializers(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'},required=True,write_only=True)
    password2 = serializers.CharField(style={'input_type': 'password'},write_only=True,label="Confirm Password")
    class Meta:
        model = User
        fields = ["username","email","password","password2"]
        extra_kwargs = {
            'password': {'write_only': True}
        }
    def create(self,validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        password2 = validated_data['password2']
        if (email and User.objects.filter(email=email).exclude(username=username).exists()):
            raise serializers.ValidationError({
                'email': 'must be unique'
            })
        if password != password2:
            raise serializers.ValidationError({
                'password': 'must be same'
            })
        users = User(username=username,email=email)
        users.set_password(password)
        users.save()
        return users
class AccountSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = User
