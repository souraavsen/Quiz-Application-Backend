from django.urls import path
from .views import Reistration
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('registration/', Reistration.as_view(), name="registration"),
]


"""
http://127.0.0.1:8000/accounts/login/
http://127.0.0.1:8000/accounts/registration/

"""