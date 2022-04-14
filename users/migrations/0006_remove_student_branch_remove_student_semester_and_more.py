# Generated by Django 4.0.3 on 2022-04-14 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_branch_semester_remove_student_academic_year_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='branch',
        ),
        migrations.RemoveField(
            model_name='student',
            name='semester',
        ),
        migrations.AlterField(
            model_name='role',
            name='name',
            field=models.CharField(blank=True, choices=[('SUPERADMIN', 'is_superadmin'), ('ADMIN', 'is_admin'), ('TEACHER', 'is_teacher'), ('STUDENT', 'is_student')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='semester',
            name='Academic_Year',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=5, null=True)),
                ('branch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.branch')),
                ('semester', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.semester')),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='section',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.section'),
        ),
    ]
