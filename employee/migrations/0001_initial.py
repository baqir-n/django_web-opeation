# Generated by Django 3.2.9 on 2021-11-11 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.CharField(max_length=20)),
                ('ename', models.CharField(max_length=255)),
                ('eemail', models.CharField(max_length=255)),
                ('econtact', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'employee',
            },
        ),
    ]
