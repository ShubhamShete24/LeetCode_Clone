from django.contrib.auth.models import User
from rest_framework import serializers


class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'required': True
            },
            'first_name': {
                'required': True
            },
            'last_name': {
                'required': True
            },
            'email': {
                'required': True
            }
        }

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['email'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

