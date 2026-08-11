from rest_framework import serializers
from academy.models import Teacher

class TeacherSerializer(serializers.ModelSerializer):

    class Meta:

        model = Teacher
        fields = [
            "id",
            "name",
            "email",
            "specialty",
        ]
        read_only_fields = ["id","email"]