# Generated by Django 3.2.6 on 2021-09-09 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course_management', '0015_quiz_ques_answer_quiz_question'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quiz_question',
            old_name='category_id',
            new_name='chapter_id',
        ),
    ]