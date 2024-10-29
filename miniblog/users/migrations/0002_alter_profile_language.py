# Generated by Django 5.0.7 on 2024-10-07 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='language',
            field=models.CharField(choices=[('en', 'English'), ('es', 'Español')], default='en', max_length=30),
        ),
    ]