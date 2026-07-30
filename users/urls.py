from django.urls import path
from users.views import RegisterView
from users.views import LoginView, CookieTokenRefreshView, UserMeView
urlpatterns = [
    path('register/', view = RegisterView.as_view()),
    path('token/', LoginView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', CookieTokenRefreshView.as_view(), name='token_refresh'),
    path('auth/', UserMeView.as_view(), name='auth'),
]