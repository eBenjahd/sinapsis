from django.db import models
from django.contrib.auth.models import User
from .course_model import Course

class Enrollment(models.Model):

    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="enrollments")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="enrollments")
    progress = models.PositiveIntegerField(default=0)
    completed = models.BooleanField(default=False)
    enrolled_at = models.DateTimeField(auto_now_add=True)
