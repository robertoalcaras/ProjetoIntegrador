# Generated by Django 3.2.8 on 2021-11-17 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ataquevocal', '0001_initial'),
        ('avaliacaoAD', '0008_ressonanciacad'),
    ]

    operations = [
        migrations.CreateModel(
            name='AtaqueVocalCad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resposta', models.CharField(choices=[('S', 'Sim'), ('N', 'Nâo')], default='N', max_length=1)),
                ('ataquevocal', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ataquevocal.ataquevocal')),
                ('avaliacaoAD', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='avaliacaoAD.avaliacaoad')),
            ],
        ),
    ]
