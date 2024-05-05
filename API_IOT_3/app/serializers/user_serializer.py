from rest_framework import serializers
from app.models.user_model import UserLogin

class UserLoginSerializer(serializers.ModelSerializer):
  class Meta:
    model = UserLogin
    fields = '__all__'