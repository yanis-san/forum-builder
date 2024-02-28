from django.urls import path
from authentication.views import login_page, logout_user, signup_forum

app_name = "authentication"

urlpatterns = [
    path("login/", login_page, name="login"),
    path("logout/", logout_user, name="logout"),
    path("signup/", signup_forum, name="signup-forum"),

]
