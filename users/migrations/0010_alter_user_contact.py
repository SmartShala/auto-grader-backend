# Generated by Django 4.0.3 on 2022-04-22 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_user_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='contact',
            field=models.BigIntegerField(default=0, unique=True),
        ),
    ]
