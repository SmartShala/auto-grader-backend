# Generated by Django 4.0.3 on 2022-04-14 21:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Test_module', '0002_questions_created_at_questions_updated_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Test_module.subject'),
        ),
    ]
