# Generated by Django 3.2.3 on 2021-05-27 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('models_app', '0004_auto_20210527_1005'),
    ]

    operations = [
        migrations.RenameField(
            model_name='school',
            old_name='name',
            new_name='school_name',
        ),
    ]