
from dataclasses import field
from rest_framework import serializers
from .models import Test, Test2

class TestSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Test
        fields = '__all__'

class Test2Serializer(serializers.ModelSerializer):
    largecount = TestSerializer()
    class Meta:
        model = Test2
        fields = '__all__'

    # def create(self, validated_data):
    #     largecount_data = validated_data.pop('largecount')
    #     test2 = Test2.objects.create(**validated_data)
    #     Profile.objects.create(user=user, **profile_data)
    #     return user

