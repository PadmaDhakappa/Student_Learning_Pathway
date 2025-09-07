from rest_framework import serializers
from . import models

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UsersPublic
        fields = ["email", "username", "created_at"]

class EnrollmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Enrollments
        fields = "__all__"

class AssessmentsEolSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AssessmentsEol
        fields = "__all__"

class AssessmentsFaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AssessmentsFa
        fields = "__all__"

class AssessmentsSaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AssessmentsSa
        fields = "__all__"

class SubjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Subjects
        fields = "__all__"

class AssessmentWeightsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AssessmentWeights   # match the exact class name from inspectdb
        fields = "__all__"
