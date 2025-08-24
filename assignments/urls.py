from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import AssignmentViewSet, submit_assignment, grade_submission

router = DefaultRouter()
router.register(r"assignments", AssignmentViewSet, basename="assignment")

urlpatterns = router.urls + [
    path("submissions/", submit_assignment, name="submit_assignment"),
    path("submissions/<int:submission_id>/grade/", grade_submission, name="grade_submission"),
]
