# Generated by Django 3.2.9 on 2021-11-12 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='password',
            field=models.CharField(default='SOME STRING', max_length=30),
        ),
        migrations.AddField(
            model_name='employee',
            name='repassword',
            field=models.CharField(default='SOME STRING', max_length=30),
        ),
    ]
