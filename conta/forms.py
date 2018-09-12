from django import forms
from django.contrib.auth.forms import UserCreationForm

from controle.models import *

class CadastroForm(UserCreationForm):
 
	chefe = forms.BooleanField(label='É chefe de setor ?', required=False)
	setor = forms.CharField(label='Setor', max_length=100)
	email = forms.EmailField(label='E-mail')
	chefe_imediato = forms.ModelChoiceField(queryset=Funcionario.objects.filter(chefe=True) ,empty_label='Informe seu chefe', required=False)
	hora_padrao = forms.ModelChoiceField(queryset=HoraPadrao.objects.all(), empty_label='Informe horário')

	def save(self, commit=True):
		user = super(CadastroForm, self).save(commit=False)
		funcionario = Funcionario()
		funcionario.chefe = self.cleaned_data['chefe']
		funcionario.setor = self.cleaned_data['setor']
		user.email = self.cleaned_data['email']
		#funcionario.chefe_imediato = self.cleaned_data['chefe_imediato']
		funcionario.horaPadrao = self.cleaned_data['hora_padrao']
		if commit :
			user.save()
			funcionario.save()
		return user
