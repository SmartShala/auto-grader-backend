# Generated by Django 4.0.3 on 2022-04-14 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing_page', '0002_querydata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='querydata',
            name='email',
            field=models.EmailField(blank=True, error_messages={'unique': 'This email already exists!'}, max_length=254, null=True, unique=True),
        ),
    ]
