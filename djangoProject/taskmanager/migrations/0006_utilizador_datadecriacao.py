# Generated by Django 4.2.1 on 2023-05-12 05:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0005_utilizador_tarefasconcluidas_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='utilizador',
            name='datadecriacao',
            field=models.DateField(default=datetime.date(2023, 5, 12)),
        ),
    ]
