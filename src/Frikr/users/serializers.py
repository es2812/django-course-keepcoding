from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.Serializer):
    
    id = serializers.ReadOnlyField() # id cannot be edited
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def create(self, validated_data):
        """
        Creates an user instance from validated_data containing deserialized data.
        :param validated_data: Dict with user data
        :return object User
        """

        instance = User()
        return self.update(instance, validated_data)

    def update(self, instance, validated_data):
        """
        Updates an user instance from validated_data containing deserialized data.
        :param instance: User object to update
        :param validated_data: Dict with user data
        :return object User
        """

        instance.first_name = validated_data.get("first_name")
        instance.last_name = validated_data.get("last_name")
        instance.username = validated_data.get("username")
        instance.email = validated_data.get("email")
        instance.set_password(validated_data.get("password"))

        instance.save()
        return instance

    def validate_username(self, data):
        users = User.objects.filter(username=data)

        # if we are creating (there's no instance on self) check if username exists
        # if we are updating, and the new username is different from instance (username is being changed) and there's already users registered with that username
        if (not(self.instance) or self.instance.username != data) and len(users)!=0:
            raise serializers.ValidationError("Ya existe un usuario con ese username")
        else:
            return data