from rest_framework import serializers
from ProblemCreation.models import *


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ["topicName"]


class DifficultyLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DifficultyLevel
        fields = ["diffLevel"]


class ProblemCreationSerializer(serializers.ModelSerializer):
    topicID = TopicSerializer
    diffID = DifficultyLevelSerializer

    class Meta:
        model = ProblemCreation
        fields = '__all__'
