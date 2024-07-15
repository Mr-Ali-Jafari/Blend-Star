from django.urls import path 
from . import views
urlpatterns = [
    path("profile/<int:pk>/",views.profile_detail,name="profile_detail"),
    path("c/e/profile/",views.create_or_edit_profile,name="c_e_profile"),
    path("login/",views.login_view,name="login"),
    path("register/",views.register_view,name="register"),
    path("logout/",views.logout_view,name="logout"),


]