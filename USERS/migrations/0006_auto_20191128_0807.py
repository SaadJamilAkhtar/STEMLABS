# Generated by Django 2.2.6 on 2019-11-28 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('USERS', '0005_auto_20191124_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='blood_group',
            field=models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], max_length=3),
        ),
        migrations.AlterField(
            model_name='users',
            name='image',
            field=models.ImageField(default='images/profile/default_profile_kylie.jpg', upload_to='images/profile'),
        ),
    ]
