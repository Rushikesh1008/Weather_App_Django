from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home),
    path('reset/',views.reset),
    path('about/',views.about),
    path('contact/',views.contact),
    path('signup/',views.signup_view, name='signup'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('account/',views.account_view,name='account'),
]
