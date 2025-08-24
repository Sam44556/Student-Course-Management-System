from django.db import models
from courses.models import Course
from accounts.models import User

class Assignment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateTimeField()

    def __str__(self):
        return f"{self.title} ({self.course.title})"

class Submission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name="submissions")
    student = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={"role": "student"})
    file = models.FileField(upload_to="submissions/")
    submitted_at = models.DateTimeField(auto_now_add=True)
    grade = models.FloatField(null=True, blank=True)

    class Meta:
        unique_together = ("assignment", "student")  # Prevent multiple submissions

    def __str__(self):
        return f"{self.student.username} - {self.assignment.title}"
