# Generated by Django 5.1.7 on 2025-03-25 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_course_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='statement',
            field=models.URLField(blank=True),
        ),
    ]
