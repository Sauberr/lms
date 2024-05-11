from django.urls import path

from user_account.views import UserLoginView, UserLogoutView, UserRegistrationView, ActivateUser

app_name = 'user_account'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    path("activate/<str:uuid64>/<str:token>/", ActivateUser.as_view(), name="activate_user"),
]
