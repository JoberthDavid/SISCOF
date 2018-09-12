# Generated by Django 2.0.2 on 2018-06-30 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Frequencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ipComputador', models.GenericIPAddressField()),
                ('data', models.DateField(auto_now=True, verbose_name='Data')),
                ('horaEntradaExpediente1', models.TimeField(blank=True, null=True, verbose_name='Hora entrada primeiro expediente')),
                ('horaSaidaExpediente1', models.TimeField(blank=True, null=True, verbose_name='Hora saída primeiro expediente')),
                ('horaEntradaExpediente2', models.TimeField(blank=True, null=True, verbose_name='Hora entrada segundo expediente')),
                ('horaSaidaExpediente2', models.TimeField(blank=True, null=True, verbose_name='Hora saída segundo expediente')),
                ('horaEntradaExpedienteExtra', models.TimeField(blank=True, null=True, verbose_name='Hora entrada expediente extra')),
                ('horaSaidaExpedienteExtra', models.TimeField(blank=True, null=True, verbose_name='Hora saída expediente extra')),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=100, null=True, verbose_name='email')),
                ('chefe', models.BooleanField(default=False, verbose_name='Chefe ?')),
                ('setor', models.CharField(max_length=20, verbose_name='Setor')),
            ],
        ),
        migrations.CreateModel(
            name='HoraPadrao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=50, verbose_name='Descrição hora padrão')),
                ('horaEntradaExpediente1', models.TimeField()),
                ('horaSaidaExpediente1', models.TimeField()),
                ('horaEntradaExpediente2', models.TimeField()),
                ('horaSaidaExpediente2', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Justificativa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('justificativa', models.CharField(max_length=300, verbose_name='Justificativa')),
            ],
        ),
        migrations.CreateModel(
            name='Situacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('situacao', models.CharField(choices=[('AC', 'Aceitável'), ('IN', 'Inaceitável'), ('NA', 'Não avaliado')], default='NA', max_length=2, verbose_name='Situação')),
                ('chefe', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='controle.Funcionario')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('IE', 'Inconsistente'), ('CO', 'Concistente')], default='CO', max_length=2, verbose_name='Status')),
            ],
        ),
        migrations.AddField(
            model_name='justificativa',
            name='situacao',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='controle.Situacao'),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='horaPadrao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='controle.HoraPadrao'),
        ),
        migrations.AddField(
            model_name='frequencia',
            name='funcionario',
            field=models.ManyToManyField(to='controle.Funcionario'),
        ),
        migrations.AddField(
            model_name='frequencia',
            name='justificativa',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='controle.Justificativa'),
        ),
        migrations.AddField(
            model_name='frequencia',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='controle.Status'),
        ),
    ]
