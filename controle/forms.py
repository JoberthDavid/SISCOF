from django import forms
from django.core.mail import send_mail
from django.conf import settings

class Contato(forms.Form):

	nome = forms.CharField(label="Nome", max_length=100)
	email = forms.EmailField(label="email")
	mensagem = forms.CharField(label="Mensagem", widget=forms.Textarea)

	def send_mail(self):
		assunto = 'SISCOF - contato'
		mensagem = 'Nome: %(nome)s;Email: %(email)s;%(mensagem)s'
		context = {
			'nome': self.cleaned_data['nome'],
			'email': self.cleaned_data['email'],
			'mensagem': self.cleaned_data['mensagem'],
		}
		mensagem = mensagem % context
		send_mail(assunto, mensagem, settings.DEFAULT_FROM_EMAIL, settings.CONTATO_EMAIL)