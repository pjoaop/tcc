# Generated by Django 4.1 on 2022-10-02 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_ocupacao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='ocupacao',
        ),
    ]
