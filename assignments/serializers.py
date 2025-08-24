from rest_framework import serializers
from .models import Assignment, Submission

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ["id", "course", "title", "description", "due_date"]

class SubmissionSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source="student.username", read_only=True)

    class Meta:
        model = Submission
        fields = ["id", "assignment", "student", "student_name", "file", "submitted_at", "grade"]
        read_only_fields = ["submitted_at", "grade"]
