# Generated by Django 5.1.2 on 2024-11-24 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0003_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='zipCode',
            field=models.IntegerField(),
        ),
    ]
