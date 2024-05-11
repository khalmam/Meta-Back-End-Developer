# Generated by Django 4.2.11 on 2024-05-01 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('contact', models.CharField(max_length=200, verbose_name='Phone Number')),
                ('guest_count', models.IntegerField()),
                ('time', models.TimeField()),
                ('notes', models.CharField(blank=True, max_length=300)),
            ],
        ),
        migrations.DeleteModel(
            name='Booking',
        ),
    ]