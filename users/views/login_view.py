from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response


class LoginView(TokenObtainPairView):

    def post(self, request, *args, **kwargs):

        response = super().post(request, *args, **kwargs)

        refresh_token = response.data["refresh"]
        access_token = response.data["access"]

        new_response = Response({
            "message": "Login correcto"
        })

        new_response.set_cookie(
            key="access_token",
            value=access_token,
            httponly=True,
            secure=True,
            samesite="Lax",
            max_age=60 * 1
        )

        new_response.set_cookie(
            key="refresh_token",
            value=refresh_token,
            httponly=True,
            secure=True,
            samesite="Lax",
            max_age=60 * 5
        )

        return new_response