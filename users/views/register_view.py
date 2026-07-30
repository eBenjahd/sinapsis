from rest_framework.generics import CreateAPIView

from rest_framework.response import Response

from rest_framework_simplejwt.tokens import RefreshToken

from users.serializers import RegisterSerializer

class RegisterView(CreateAPIView):

    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        access = refresh.access_token

        response = Response({
            "message": "Usuario creado correctamente"
        })

        response.set_cookie(
            key="access_token",
            value=str(access),
            httponly=True,
            secure=True,
            samesite="Lax",
        )

        response.set_cookie(
            key="refresh_token",
            value=str(refresh),
            httponly=True,
            secure=True,
            samesite="Lax",
        )

        return response