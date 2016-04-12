from rest_framework import serializers
from django.contrib.auth.models import User
from florist_app.models import Arrangement, Basket, Florist, Buyer


class ArrangementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Arrangement


class BasketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Basket


class FloristSerializer(serializers.ModelSerializer):

    class Meta:
        model = Florist


class BuyerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Buyer


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('first_name', 'email', 'username', 'password')

    def create(self, validated_data):
        user = User(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            if key == 'password':
                instance.set_password(value)
            else:
                setattr(instance, key, value)
        instance.save()
        return instance
