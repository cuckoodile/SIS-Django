# Generated by Django 5.1.2 on 2024-11-08 04:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='students',
            old_name='name',
            new_name='studentName',
        ),
    ]
