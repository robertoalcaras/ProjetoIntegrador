# Generated by Django 3.2.8 on 2021-10-11 15:03

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('paciente', '0003_delete_avaliacaoad'),
    ]

    operations = [
        migrations.CreateModel(
            name='AvaliacaoAD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DataAvaliacao', models.DateTimeField(default=datetime.datetime.now)),
                ('QOrelha', models.CharField(max_length=5)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='paciente.paciente')),
            ],
        ),
    ]
