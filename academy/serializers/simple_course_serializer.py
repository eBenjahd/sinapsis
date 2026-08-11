from rest_framework import serializers
from academy.models import Course

class CourseSimpleSerializer(serializers.ModelSerializer):

    # student_count = serializers.IntegerField(read_only=True)
    average_rating = serializers.FloatField(read_only=True)
    class Meta:

        model = Course
        fields = ["id", "title", "price","average_rating"]