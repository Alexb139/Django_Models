# Generated by Django 3.2.3 on 2021-05-27 15:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('models_app', '0005_rename_name_school_school_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='last_name',
        ),
        migrations.AddField(
            model_name='student',
            name='full_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
