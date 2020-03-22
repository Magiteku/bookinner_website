# Generated by Django 3.0.3 on 2020-03-12 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_membre_mail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membre',
            name='mail',
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterField(
            model_name='membre',
            name='nom',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='membre',
            name='prenom',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
