# Generated by Django 3.0.3 on 2020-03-12 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_auto_20200312_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membre',
            name='mail',
            field=models.EmailField(blank=True, max_length=50, null=True),
        ),
    ]
