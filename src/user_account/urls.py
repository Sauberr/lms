from django.urls import path

from user_account.views import UserLoginView, UserLogoutView, UserRegistrationView, send_test_email

app_name = 'user_account'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    path('send_test_email/', send_test_email, name='send_test_email')
]
