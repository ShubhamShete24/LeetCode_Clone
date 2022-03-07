from rest_framework import serializers
from Company.models import *
from ProblemCreation.serializers import ProblemCreationSerializer


class CompanyNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyName
        fields = ["companyName"]


class CompanyProblemSerializer(serializers.ModelSerializer):
    companyID = CompanyNameSerializer()
    problemID = ProblemCreationSerializer

    class Meta:
        model = ProblemCreation
        fields = '__all__'
