# Generated by Django 4.0.5 on 2022-06-22 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_alter_data_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data',
            old_name='id',
            new_name='ids',
        ),
    ]
