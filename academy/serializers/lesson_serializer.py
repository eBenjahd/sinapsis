from rest_framework import serializers
from academy.models import Lesson

class LessonSerializer(serializers.ModelSerializer):


    class Meta:

        model = Lesson
        fields = [
            "id",
            "title",
            "duration",
            "order",
            "course",
        ]

        read_only_fields= ["id","order"]