from django.urls import path
from .import views
urlpatterns = [

    path('show_account',views.show_account,name='account'),
    path('signin',views.signin,name='signin'),
    path('logout',views.sign_out,name='logout')

    ]