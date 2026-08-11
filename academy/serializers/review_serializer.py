from rest_framework import serializers
from academy.models import Review
from users.serializers import UserSerializer
from .simple_course_serializer import CourseSimpleSerializer


class ReviewSerializer(serializers.ModelSerializer):

    student = UserSerializer(read_only=True)
    course = CourseSimpleSerializer(read_only=True)

    class Meta:

        model = Review
        fields = [
            "id",
            "student",
            "course",
            "rating",
            "comment",
        ]

        read_only_fields = ["id"]