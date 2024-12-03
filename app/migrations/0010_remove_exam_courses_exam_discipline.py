# Generated by Django 5.1.3 on 2024-11-22 22:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_remove_list_topic_question_topic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam',
            name='courses',
        ),
        migrations.AddField(
            model_name='exam',
            name='discipline',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.discipline'),
        ),
    ]
