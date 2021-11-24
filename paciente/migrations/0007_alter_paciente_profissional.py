# Generated by Django 3.2.8 on 2021-11-19 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ProfissionalEnc', '0003_profissionalenc_status'),
        ('paciente', '0006_alter_paciente_sexo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='Profissional',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProfissionalEnc.profissionalenc'),
        ),
    ]
