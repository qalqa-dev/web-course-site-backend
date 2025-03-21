# Generated by Django 5.1.7 on 2025-03-21 12:53

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_mentor_person_alter_teacher_person'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='person',
        ),
        migrations.CreateModel(
            name='MentorProfile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='mentor_profile', to='app.person')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TeacherProfile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_profile', to='app.person')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Mentor',
        ),
        migrations.DeleteModel(
            name='Teacher',
        ),
    ]
