# Generated by Django 3.2.8 on 2021-11-17 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ressonancia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name_plural': 'Tipo de Ressonacia',
            },
        ),
    ]
