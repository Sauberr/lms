from django.contrib.auth import login, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.views.generic import CreateView, RedirectView, DetailView

from students.utils.token_generator import TokenGenerator
from user_account.forms import UserRegistrationForm
from user_account.services.emails import send_registration_email

from user_account.models import UserProfile


class UserLoginView(LoginView):
    ...


class UserLogoutView(LogoutView):
    ...


class UserRegistrationView(CreateView):
    template_name = "registration/registration.html"
    model = get_user_model()
    form_class = UserRegistrationForm
    success_url = reverse_lazy("user_account:login")

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.is_active = False
        self.object.save()
        send_registration_email(request=self.request, user_instance=self.object)
        return super().form_valid(form)


class UserProfileView(LoginRequiredMixin, DetailView):
    template_name = "registration/user_profile.html"
    pk_url_kwarg = 'pk'
    model = UserProfile
    queryset = UserProfile.objects.all()


class ActivateUser(RedirectView):
    url = reverse_lazy("index")

    def get(self, request, uuid64, token, *args, **kwargs):

        try:
            pk = force_str(urlsafe_base64_decode(uuid64))
            current_user = get_user_model().objects.get(pk=pk)
        except (ValueError, get_user_model().DoestNotExist, TypeError):
            return HttpResponse("Activation link is invalid")

        if current_user and TokenGenerator().check_token(current_user, token):
            current_user.is_active = True
            current_user.save()
            login(request, current_user)

            return super().get(request, *args, **kwargs)

        return HttpResponse("Activation link is invalid")
