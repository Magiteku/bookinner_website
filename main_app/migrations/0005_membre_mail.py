# Generated by Django 3.0.3 on 2020-03-12 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20200305_1809'),
    ]

    operations = [
        migrations.AddField(
            model_name='membre',
            name='mail',
            field=models.EmailField(default=None, max_length=50),
        ),
    ]
