from rest_framework import viewsets, permissions
from .models import Course
from .serializers import CourseSerializer
from rest_framework.response import Response

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow only admins to create/update/delete courses.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.role == "admin"

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAdminOrReadOnly]

    def perform_create(self, serializer):
        serializer.save()
