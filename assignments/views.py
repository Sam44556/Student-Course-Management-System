from rest_framework import viewsets, permissions
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from .models import Assignment, Submission
from .serializers import AssignmentSerializer, SubmissionSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404

# Assignment CRUD (Instructor only for create/update/delete)
class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Optional: check if user is instructor
        serializer.save()

# Submission endpoints
@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def submit_assignment(request):
    student = request.user
    assignment_id = request.data.get("assignment")
    file = request.FILES.get("file")

    assignment = get_object_or_404(Assignment, id=assignment_id)
    submission, created = Submission.objects.get_or_create(
        assignment=assignment, student=student,
        defaults={"file": file}
    )
    if not created:
        return Response({"message": "Already submitted"}, status=status.HTTP_400_BAD_REQUEST)

    serializer = SubmissionSerializer(submission)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(["PATCH"])
@permission_classes([permissions.IsAuthenticated])
def grade_submission(request, submission_id):
    submission = get_object_or_404(Submission, id=submission_id)
    grade = request.data.get("grade")

    # Optional: check if request.user is instructor of the assignment
    submission.grade = grade
    submission.save()
    serializer = SubmissionSerializer(submission)
    return Response(serializer.data)
