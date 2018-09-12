from django.urls import path
from controle.views import *

urlpatterns = [

	path('', index, name='index'),
	path('contato/', contato, name='contato'),
	path('ponto/', ponto, name='ponto'),
	path('funcionarios/', funcionarios, name='funcionarios'),

]