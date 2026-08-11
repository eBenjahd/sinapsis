from rest_framework import serializers
from academy.models import Course
from .teacher_serializer import TeacherSerializer
from .lesson_serializer import LessonSerializer

class CourseSerializer(serializers.ModelSerializer):

    teacher = TeacherSerializer(read_only=True)
    lessons = LessonSerializer(many=True, read_only=True)

    class Meta:

        model = Course
        fields = [
            "id",
            "title",
            "description",
            "price",
            "teacher",
            "lessons",
        ]