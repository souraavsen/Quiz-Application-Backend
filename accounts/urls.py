from django.urls import path
from .views import Reistration, UserOperation
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('login/', obtain_auth_token),
    path('registration/', Reistration.as_view()),
    path('user_operation/<str:username>/', UserOperation.as_view()),
]


"""
http://127.0.0.1:8000/accounts/login/
http://127.0.0.1:8000/accounts/registration/
http://127.0.0.1:8000/accounts/user_operation/rahul/

"""