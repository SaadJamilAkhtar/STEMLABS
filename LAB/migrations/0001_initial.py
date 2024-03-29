# Generated by Django 2.2.6 on 2019-11-28 03:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('USERS', '0006_auto_20191128_0807'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('charges', models.IntegerField()),
                ('average_value', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Appointments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apply_date', models.DateField(auto_now_add=True)),
                ('appointment_date', models.DateField()),
                ('requirements', models.BooleanField(default=False)),
                ('progress', models.CharField(choices=[('Pending', 'Pending'), ('In Progress', 'In Progress'), ('Waiting for receiver', 'Waiting for receiver'), ('Delivered', 'Delivered')], max_length=50)),
                ('delivery_date', models.DateField()),
                ('result', models.FileField(upload_to='files/results')),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='USERS.Patient')),
                ('test_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LAB.Test')),
            ],
        ),
    ]
