# Generated by Django 3.2.9 on 2021-11-19 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0005_remove_user_ucontact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uemail',
            field=models.CharField(default=False, max_length=255),
        ),
    ]
