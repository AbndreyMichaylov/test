from rest_framework import serializers
from .models import Survey, Answer

class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        exclude = ('copied', 'status')
    questions = serializers.StringRelatedField(many=True)

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'
    survey = serializers.PrimaryKeyRelatedField(read_only=True)

class AnswerOneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'    
