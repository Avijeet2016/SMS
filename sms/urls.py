from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from rest_framework.authtoken import views as TokenView
from .views import home, user_login, user_logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('login', user_login, name="login"),
    path('logout', user_logout, name='logout'),

    path('student/', include('student.urls')),
    path('teacher/', include('teacher.urls')),
    path('administration/', include('administration.urls')),
    path('api/', include('api.urls')),
]


urlpatterns += [
    path('api-token-auth/', TokenView.obtain_auth_token)
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns