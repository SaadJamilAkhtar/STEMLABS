# Generated by Django 2.2.6 on 2019-11-24 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('USERS', '0003_auto_20191124_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='age',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='users',
            name='cnic',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='users',
            name='phone_number',
            field=models.CharField(max_length=15),
        ),
    ]