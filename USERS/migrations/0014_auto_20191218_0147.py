# Generated by Django 2.2.5 on 2019-12-17 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('USERS', '0013_auto_20191215_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='image',
            field=models.ImageField(default='images/profile/default_profile_image.jpg', upload_to='media/images/profile'),
        ),
    ]