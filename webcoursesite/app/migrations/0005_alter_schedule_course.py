# Generated by Django 5.1.7 on 2025-03-25 20:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_course_description_alter_course_statement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='course',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='schedule', to='app.course'),
        ),
    ]
