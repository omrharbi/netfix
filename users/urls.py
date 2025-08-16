from django.urls import path
from django.contrib.auth import views

from .forms import UserLoginForm
from . import views as v

urlpatterns = [
   path('', v.register, name='register'),
    path('register/company/', v.CompanySignUpView.as_view(), name='register_company'),
    path('register/customer/', v.CustomerSignUpView.as_view(), name='register_customer'),

    # Login URLs
    path('', v.LoginUserView, name='login_user'),        # general login or homepage
    path('login/company/', v.LoginCompanyView, name='login_company'),
    path('login/customer/', v.LoginCustomerView, name='login_customer'),
]
