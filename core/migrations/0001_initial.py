# Generated by Django 5.1 on 2024-08-12 15:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chassi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(help_text='Máximo 16 caracteres', max_length=17, verbose_name='Chassi')),
            ],
            options={
                'verbose_name': 'Chassi',
                'verbose_name_plural': 'Chassis',
            },
        ),
        migrations.CreateModel(
            name='Montadora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
            ],
            options={
                'verbose_name': 'Montadora',
                'verbose_name_plural': 'Montadoras',
            },
        ),
        migrations.CreateModel(
            name='Carro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(help_text='Máximo 30 caracteres', max_length=30, verbose_name='Modelo')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Preço')),
                ('chassi', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.chassi')),
                ('montadora', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.montadora')),
            ],
            options={
                'verbose_name': 'Carro',
                'verbose_name_plural': 'Carros',
            },
        ),
    ]
