import re

from django.contrib.auth.models import User
from rest_framework import serializers

from accounts.models import Profile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name']


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = ['user', 'phone', 'code_melli', 'gender', 'image', 'created_at']
        depth = 1

    def update(self, instance, validated_data):
        print(validated_data)
        user_data = validated_data.pop('user', validated_data)
        user = instance.user
        # print(user_data.get('first_name'))

        instance.gender = validated_data.get('gender', instance.gender)
        instance.phone = validated_data.get('gender', instance.phone)
        instance.image = validated_data.get('gender', instance.image)
        instance.save()

        user.username = user_data.get('username', user.username)
        user.first_name = user_data.get('first_name', user.first_name)
        user.last_name = user_data.get('last_name', user.last_name)
        # print(user_data.get('first_name'))
        user.save()
        return instance

    def validate_phone(self, value):
        """
        Check that phone number is correct
        """
        if value[0] == '0':
            raise serializers.ValidationError('please enter the correct number (شماره تان را بدون صفر وارد کنید)')
        if len(value) != 10:
            raise serializers.ValidationError("please enter the correct number (your number must be 10 digits)")
        if not re.search('^99[0-48]|^91[0-9]|^90[1-5]|^93[0-9]|^941|^92[0-2]', value):
            raise serializers.ValidationError('please enter the correct number (پیش شماره شما باید معتبر باشد)')
        return value
