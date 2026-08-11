from django.db import models
from .course_model import Course
class Lesson(models.Model):

    title = models.CharField(max_length=100)
    duration = models.IntegerField()
    order = models.PositiveIntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="lessons")

    def __str__(self):
        return self.title
    