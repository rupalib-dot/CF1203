# Generated by Django 3.2.6 on 2021-09-18 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_management', '0020_remove_chapter_chapter_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='chapter_video',
            field=models.FileField(blank=True, null=True, upload_to='chapter_video/', verbose_name='chapter_video'),
        ),
    ]