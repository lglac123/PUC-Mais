# Generated by Django 5.1.2 on 2024-11-19 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_question_answer_remove_question_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='answer',
            new_name='question',
        ),
    ]