from django.urls import path, include
from .views import home ,detail ,contact ,about ,login , accounthome, registrationpage
app_name = "blog"
urlpatterns = [
    path('', home, name='home'),
    path("article/<slug:slug>", detail, name='detail'),
    path("contact/", contact, name='contact'),    
    path("about/", about, name='about'),
    #path("login/", login, name='login'),
    path("signup/", registrationpage , name='signup'),
    path("accounts/", include("django.contrib.auth.urls"), name="login"),
    path("accounts/", accounthome, name='accounts'),
    #path("register/", registrationpage, name='register'),

]