from django.db import models
from accounts.models import User

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    instructor = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        limit_choices_to={"role": "instructor"},
        related_name="courses"
    )

    def __str__(self):
        return self.title
