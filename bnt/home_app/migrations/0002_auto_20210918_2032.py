# Generated by Django 3.2.6 on 2021-09-18 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='status',
        ),
        migrations.AddField(
            model_name='productattribute',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
