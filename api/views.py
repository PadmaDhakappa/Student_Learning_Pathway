from rest_framework import viewsets, permissions, filters
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from . import models
from .serializers import (
    UsersSerializer, EnrollmentsSerializer, AssessmentsEolSerializer,
    AssessmentsFaSerializer, AssessmentsSaSerializer,
    SubjectsSerializer, AssessmentWeightsSerializer
)

# ----------------------
# Base Classes
# ----------------------
class ReadOnly(viewsets.ReadOnlyModelViewSet):
    """Read-only with search & ordering"""
    permission_classes = [permissions.AllowAny]
    renderer_classes = [JSONRenderer]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]


class EnrollmentFilteredViewSet(ReadOnly):
    """
    Supports both:
      /api/<table>/                 -> all rows
      /api/<table>/<enrollment_id>/ -> rows filtered by enrollment_id
    """
    enrollment_field = "enrollment__enrollment_id"

    def list(self, request, *args, **kwargs):
        enrollment_id = kwargs.get("enrollment_id")
        if enrollment_id:
            queryset = self.queryset.filter(**{self.enrollment_field: enrollment_id})
        else:
            queryset = self.queryset.all()

        if not queryset.exists():
            return Response([], status=200)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


# ----------------------
# ViewSets
# ----------------------
class UsersViewSet(ReadOnly):
    queryset = models.UsersPublic.objects.all()
    serializer_class = UsersSerializer
    search_fields = ["email", "username"]
    ordering_fields = ["created_at", "email"]


class EnrollmentsViewSet(ReadOnly):
    queryset = models.Enrollments.objects.all()
    serializer_class = EnrollmentsSerializer
    lookup_field = "enrollment_id"    # real PK
    lookup_value_regex = r"[^/]+"


# Filtered by enrollment_id (FK → enrollment)
class AssessmentsFaViewSet(EnrollmentFilteredViewSet):
    queryset = models.AssessmentsFa.objects.all()
    serializer_class = AssessmentsFaSerializer


class AssessmentsEolViewSet(EnrollmentFilteredViewSet):
    queryset = models.AssessmentsEol.objects.all()
    serializer_class = AssessmentsEolSerializer


class AssessmentsSaViewSet(EnrollmentFilteredViewSet):
    queryset = models.AssessmentsSa.objects.all()
    serializer_class = AssessmentsSaSerializer


class SubjectsViewSet(EnrollmentFilteredViewSet):
    queryset = models.Subjects.objects.all()
    serializer_class = SubjectsSerializer


# Assessment Weights (no enrollment FK, just keep simple read-only)
class AssessmentWeightsViewSet(ReadOnly):
    queryset = models.AssessmentWeights.objects.all()
    serializer_class = AssessmentWeightsSerializer
