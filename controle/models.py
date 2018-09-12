from django.db import models
from datetime import datetime

class HoraPadrao(models.Model):
	descricao = models.CharField('Descrição hora padrão', max_length=50)
	horaEntradaExpediente1 = models.TimeField()
	horaSaidaExpediente1 = models.TimeField()
	horaEntradaExpediente2 = models.TimeField()
	horaSaidaExpediente2 = models.TimeField()

	def __str__(self):
		return self.descricao

class Funcionario(models.Model):
	chefe = models.BooleanField('Chefe ?', default=False)
	setor = models.CharField('Setor', max_length=20)
	email = models.EmailField('email', null=True, blank=True, max_length=100)
	chefe_imediato = models.ManyToManyField("self", blank=True)
	horaPadrao = models.ForeignKey(HoraPadrao, on_delete=models.CASCADE)

class Situacao(models.Model):
	ACEITAVEL = 'AC'
	INACEITAVEL = 'IN'
	NAO_AVALIADO = 'NA'
	SITUACAO_JUSTIFICATIVA_CHOICES = (
		(ACEITAVEL, 'Aceitável'),
		(INACEITAVEL, 'Inaceitável'),
		(NAO_AVALIADO, 'Não avaliado'),
	)
	chefe = models.ForeignKey(Funcionario, null=True, blank=True, on_delete=models.CASCADE)

	situacao = models.CharField('Situação', choices=SITUACAO_JUSTIFICATIVA_CHOICES, default=NAO_AVALIADO, max_length=2)

	def __str__(self):
		return self.situacao

class Justificativa(models.Model):
	justificativa = models.CharField('Justificativa',  max_length=300)
	situacao = models.OneToOneField(Situacao, on_delete=models.CASCADE)

	def __str__(self):
		return self.justificativa

class Status(models.Model):
	CONSISTENTE = 'CO'
	INCONSISTENTE = 'IE'
	STATUS_FREQUENCIA_CHOICES = (
		(INCONSISTENTE, 'Inconsistente'),
		(CONSISTENTE, 'Concistente'),
	)
	status = models.CharField('Status', choices=STATUS_FREQUENCIA_CHOICES, default=CONSISTENTE, max_length=2)

	def __str__(self):
		return self.status

class Frequencia(models.Model):
	funcionario = models.ManyToManyField(Funcionario)
	status = models.ForeignKey(Status, on_delete=models.CASCADE)
	ipComputador = models.GenericIPAddressField(protocol='both', unpack_ipv4=False)
	justificativa = models.OneToOneField(Justificativa, on_delete=models.CASCADE, null=True, blank=True)
	data = models.DateField('Data', auto_now=True)
	horaEntradaExpediente1 = models.TimeField('Hora entrada primeiro expediente', null=True, blank=True)
	horaSaidaExpediente1 = models.TimeField('Hora saída primeiro expediente', null=True, blank=True)
	horaEntradaExpediente2 = models.TimeField('Hora entrada segundo expediente', null=True, blank=True)
	horaSaidaExpediente2 = models.TimeField('Hora saída segundo expediente', null=True, blank=True)
	horaEntradaExpedienteExtra = models.TimeField('Hora entrada expediente extra', null=True, blank=True)
	horaSaidaExpedienteExtra = models.TimeField('Hora saída expediente extra', null=True, blank=True)

	def __str__(self):
		return self.data.strftime('%d/%m/%Y')

	def hora(self):
		return self.datetime.now()