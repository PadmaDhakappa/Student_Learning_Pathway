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
    lookup_field = "enrollment_id"    # make detail routes stable if you use them

# Composite-PK tables → list-only
class AssessmentsFaViewSet(JSONListOnly):
    queryset = models.AssessmentsFa.objects.all()
    serializer_class = AssessmentsFaSerializer

class AssessmentsEolViewSet(JSONListOnly):
    queryset = models.AssessmentsEol.objects.all()
    serializer_class = AssessmentsEolSerializer

class AssessmentsSaViewSet(JSONListOnly):
    queryset = models.AssessmentsSa.objects.all()
    serializer_class = AssessmentsSaSerializer

class SubjectsViewSet(JSONListOnly):
    queryset = models.Subjects.objects.all()
    serializer_class = SubjectsSerializer

# If assessment_weights also has a composite PK, make it list-only; if not, ReadOnly is fine
class AssessmentWeightsViewSet(JSONListOnly):
    queryset = models.AssessmentWeights.objects.all()
    serializer_class = AssessmentWeightsSerializer
