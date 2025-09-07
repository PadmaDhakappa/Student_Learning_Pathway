from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UsersViewSet, EnrollmentsViewSet, SubjectsViewSet,
    AssessmentsFaViewSet, AssessmentsEolViewSet, AssessmentsSaViewSet,
    AssessmentWeightsViewSet
)

router = DefaultRouter()
router.register(r'users', UsersViewSet, basename='users')
router.register(r'enrollments', EnrollmentsViewSet, basename='enrollments')
router.register(r'subjects', SubjectsViewSet, basename='subjects')
router.register(r'assessments_fa', AssessmentsFaViewSet, basename='assessments_fa')
router.register(r'assessments_eol', AssessmentsEolViewSet, basename='assessments_eol')
router.register(r'assessments_sa', AssessmentsSaViewSet, basename='assessments_sa')
router.register(r'assessment_weights', AssessmentWeightsViewSet, basename='assessment_weights')

urlpatterns = [
    path('', include(router.urls)),

    # Enrollment-filtered routes
    path('subjects/<str:enrollment_id>/', SubjectsViewSet.as_view({'get': 'list'})),
    path('assessments_fa/<str:enrollment_id>/', AssessmentsFaViewSet.as_view({'get': 'list'})),
    path('assessments_eol/<str:enrollment_id>/', AssessmentsEolViewSet.as_view({'get': 'list'})),
    path('assessments_sa/<str:enrollment_id>/', AssessmentsSaViewSet.as_view({'get': 'list'})),
    path('assessment_weights/<str:enrollment_id>/', AssessmentWeightsViewSet.as_view({'get': 'list'})),
]
