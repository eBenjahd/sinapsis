from django.urls import path
from users.views import RegisterView
from users.views import LoginView, CookieTokenRefreshView, UserMeView, UserView

urlpatterns = [
    path('register/', view = RegisterView.as_view()),
    path('token/', LoginView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', CookieTokenRefreshView.as_view(), name='token_refresh'),
    path('auth/', UserMeView.as_view(), name='auth'),
    path("users/", UserView.as_view({"get": "list", "post": "create",}), name="users",),
    path("users/<int:pk>/", UserView.as_view(
        { 
            "get": "retrieve", 
            "put": "update", 
            "patch": "partial_update", 
            "delete": "destroy", 
            }
        ), name="user-detail", 
    ),
]