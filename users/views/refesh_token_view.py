from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.response import Response


class CookieTokenRefreshView(TokenRefreshView):

    def post(self, request, *args, **kwargs):

        refresh_token = request.COOKIES.get("refresh_token")

        if not refresh_token:
            return Response(
                {"error": "Refresh token no encontrado"},
                status=401
            )

        request.data["refresh"] = refresh_token

        response = super().post(request, *args, **kwargs)

        access_token = response.data["access"]

        new_response = Response({
            "message": "Token actualizado"
        })

        new_response.set_cookie(
            key="access_token",
            value=access_token,
            httponly=True,
            secure=True,
            samesite="Lax",
            max_age=60 * 1
        )

        return new_response