from rest_framework import serializers
from .models import User,Profile

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email','password']

class StaffRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email','username','firstname','lastname','password','restaurant']

class CustomerRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email','username','firstname','lastname','password']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user','address','contact_number']