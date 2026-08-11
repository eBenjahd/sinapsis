from django.contrib import admin
from .models import Enrollment, Review, Teacher, Course, Lesson

admin.site.register(Enrollment)
admin.site.register(Review)
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Lesson)
