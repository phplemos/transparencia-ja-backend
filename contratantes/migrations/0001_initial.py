# Generated by Django 5.1.3 on 2024-11-24 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contratantes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('cnpj', models.CharField(max_length=18, unique=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
    ]
