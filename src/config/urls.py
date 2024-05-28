from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from students.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path("admin/", admin.site.urls),
    path("students/", include("students.urls")),
    path("groups/", include("groups.urls")),
    path("teachers/", include("teachers.urls")),
    path("users/", include("user_account.urls")),
    path("oauth/", include("social_django.urls", namespace="social")),
    path('i18n/', include('django.conf.urls.i18n')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns.append(path("__debug__/", include("debug_toolbar.urls"))),
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
