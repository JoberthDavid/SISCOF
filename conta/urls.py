from django.urls import path
from conta.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('entrar', auth_views.LoginView.as_view(template_name='login.html'), name='entrar'),
	# path('entrar', do_login, name='entrar'),
	path('', do_logout, name='sair'),
	path('cadastro', cadastro, name='cadastro'),

]