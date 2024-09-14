from rest_framework import serializers

from .models import User, Level, Card, Tasks

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class LevelSer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'

class CardSer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'

class TaskSer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'