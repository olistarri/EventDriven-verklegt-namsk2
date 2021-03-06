from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views
from forms.forms import CustomAuthForm

urlpatterns = [
    path('login', LoginView.as_view(
        template_name='user/login.html',
        authentication_form=CustomAuthForm),
        name="login_page"),
    path('register', views.register, name="register"),
    path('logout', LogoutView.as_view(next_page='login_page'), name='logout'),
    path('edituser', views.update_user, name="edit_user"),
    path('changepassword', views.change_password, name='change_password'),
    path('profile', views.profile, name='users_profile'),
    #path('changepassword', views.change_password, name='change_password')

]
