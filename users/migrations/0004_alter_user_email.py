# Generated by Django 4.0.3 on 2022-04-10 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(default='abc@xyz.com', max_length=100, unique=True),
        ),
    ]
