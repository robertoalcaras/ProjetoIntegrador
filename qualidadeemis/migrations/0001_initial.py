# Generated by Django 3.2.8 on 2021-11-18 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Qualidadeemis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name_plural': 'Qualidade na Emissão',
            },
        ),
    ]
