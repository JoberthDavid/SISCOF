from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from django.conf import settings

from .forms import CadastroForm

# def do_login(request):
#     context = {
#         'form' : AuthenticationForm()
#     }

#     if request.method == 'POST':
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('/ponto')
#         else:
#             return redirect("/")

#     return render(request, "login.html", context)

@login_required
def do_logout(request):
    logout(request)
    return redirect('index')

def cadastro(request):
	if request.method == 'POST':
		form = CadastroForm(request.POST)
		if form.is_valid():
			user = form.save()
			user = authenticate(username=user.username, password=form.cleaned_data['password1'])
			login(request, user)
			return redirect('ponto')
	else:
		form = CadastroForm()
	context = {
		'form' : form
	}
	return render(request, "cadastro.html", context)