from rest_framework import serializers
from academy.models import Enrollment


class EnrollmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Enrollment
        fields = [
            "id",
            "student",
            "course",
            "progress",
            "completed",
            "enrolled_at",
        ]

        read_only_fields = [
            "id",
            "enrolled_at",
        ]