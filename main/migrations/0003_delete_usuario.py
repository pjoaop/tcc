# Generated by Django 4.1 on 2022-10-01 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_questao_titulo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]
