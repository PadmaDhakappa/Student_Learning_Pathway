from rest_framework import viewsets, permissions, filters, mixins
from rest_framework.renderers import JSONRenderer
from . import models
from .serializers import (
    UsersSerializer, EnrollmentsSerializer, AssessmentsEolSerializer,
    AssessmentsFaSerializer, AssessmentsSaSerializer,
    SubjectsSerializer, AssessmentWeightsSerializer
)

class JSONListOnly(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = [permissions.AllowAny]
    renderer_classes = [JSONRenderer]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]

class ReadOnly(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.AllowAny]
    renderer_classes = [JSONRenderer]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]

# Safe users (from view)
class UsersViewSet(ReadOnly):
    queryset = models.UsersPublic.objects.all()
    serializer_class = UsersSerializer
    search_fields = ["email", "username"]
    ordering_fields = ["created_at", "email"]

# Single-PK table → ok to keep full read-only
class EnrollmentsViewSet(ReadOnly):
    queryset = models.Enrollments.objects.all()
    serializer_class = EnrollmentsSerializer
    lookup_field = "enrollment_id"    # stable detail routes

# Assessments (fetch all + individual by enrollment_id)
class AssessmentsFaViewSet(ReadOnly):
    queryset = models.AssessmentsFa.objects.all()
    serializer_class = AssessmentsFaSerializer
    lookup_field = "enrollment_id"

class AssessmentsEolViewSet(ReadOnly):
    queryset = models.AssessmentsEol.objects.all()
    serializer_class = AssessmentsEolSerializer
    lookup_field = "enrollment_id"

class AssessmentsSaViewSet(ReadOnly):
    queryset = models.AssessmentsSa.objects.all()
    serializer_class = AssessmentsSaSerializer
    lookup_field = "enrollment_id"

# Subjects (list + detail if single PK exists)
class SubjectsViewSet(ReadOnly):
    queryset = models.Subjects.objects.all()
    serializer_class = SubjectsSerializer
    lookup_field = "subject_id"   # adjust if your model has a different PK

# Assessment Weights
class AssessmentWeightsViewSet(ReadOnly):
    queryset = models.AssessmentWeights.objects.all()
    serializer_class = AssessmentWeightsSerializer
    lookup_field = "enrollment_id"   # adjust to the correct PK field
