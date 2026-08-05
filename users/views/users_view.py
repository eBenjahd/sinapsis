from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from users.serializers.users_serializer import UserSerializer
from rest_framework.response import Response


"""
    APIView es para crear uno sus propios metodoa
    [GET,POST,PUT, etc]
    EN CASO DE PAGINACION SE TIENE QUE FORMATEAR MANUALMENTE
    YA QUE NO HACE CASO A LO QUE ES UN PAGINATION POR DEFAULT 
    EN SETTINGS.PY
"""
# class UserView(APIView):

#     def get(self, request):
#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return Response(serializer.data)


class UserView(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
