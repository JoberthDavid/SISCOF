from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.conf import settings

from controle.models import *
from .forms import Contato

def index(request):
	return render(request, 'index.html')

def contato(request):
	context = {}
	if request.method == 'POST':
		form = Contato(request.POST)
		if form.is_valid():
			context['is_valid'] = True
			form = Contato()
	else:
		form = Contato()
	context['form'] = form
	context['contato'] = contato
	context['contato_email'] = settings.EMAIL_HOST_USER
	return render(request, 'contato.html', context)

@login_required
def ponto(request):
	frequencia = Frequencia.objects.all()
	context = {
		'frequencia' : Frequencia
	}
	return render(request, 'ponto.html', context)

@login_required
def funcionarios(request):
	lista_funcionarios = Funcionario.objects.all()
	context = { 'funcionarios' : lista_funcionarios }
	return render(request, 'funcionarios.html', context)