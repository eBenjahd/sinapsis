from academy.serializers import TeacherSerializer
from rest_framework.generics import CreateAPIView

class CreateTeacherView(CreateAPIView):

    serializer_class = TeacherSerializer
