"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from api import views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

router = SimpleRouter()
router.register(r'users', views.UsersViewSet, basename='users')
router.register(r'enrollments', views.EnrollmentsViewSet, basename='enrollments')
router.register(r'assessments_eol', views.AssessmentsEolViewSet, basename='assessments_eol')
router.register(r'assessments_fa', views.AssessmentsFaViewSet, basename='assessments_fa')
router.register(r'assessments_sa', views.AssessmentsSaViewSet, basename='assessments_sa')
router.register(r'subjects', views.SubjectsViewSet, basename='subjects')
router.register(r'assessment_weights', views.AssessmentWeightsViewSet, basename='assessment_weights')  # or 'asessment_weights' if that's your object

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),       # OpenAPI JSON
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema')),   # Swagger UI
    path('api/', include(router.urls)),
]
