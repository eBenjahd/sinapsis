from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from django.contrib.auth.models import User
from users.serializers.users_serializer import UserSerializer
from rest_framework.response import Response
from django.db.models import Q


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


class UserActiveView(ListAPIView): 

    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer


class UserDateView(ListAPIView):

    serializer_class = UserSerializer

    def get_queryset(self):
        
        query = self.request.query_params.get('created_after','')

        if not query :

            return User.objects.none()
        
        data = User.objects.filter(date_joined__gt = query)

        return data
    

class SearchUsersView(ListAPIView):

    serializer_class = UserSerializer

    def get_queryset(self):

        query = self.request.query_params.get('username')

        if not query:

            return User.objects.none()
        
        user_username = User.objects.filter(username__icontains=query)

        return user_username


class SearchEmailView(ListAPIView):

    serializer_class = UserSerializer

    def get_queryset(self):

        query = self.request.query_params.get('search')

        if not query:

            return User.objects.none()
        
        return User.objects.filter(
            Q(email__icontains = query) |
            Q(username__icontains = query)
        )