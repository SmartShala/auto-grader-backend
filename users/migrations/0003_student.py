# Generated by Django 4.0.3 on 2022-04-03 19:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_user_counter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.BigIntegerField(default=0, unique=True)),
                ('name', models.TextField(blank=True, null=True)),
                ('section', models.CharField(blank=True, max_length=1, null=True)),
                ('academic_year', models.SmallIntegerField(blank=True, null=True)),
                ('semester', models.SmallIntegerField(blank=True, null=True)),
                ('roll_no', models.SmallIntegerField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'student',
            },
        ),
    ]
