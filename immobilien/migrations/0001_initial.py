# Generated by Django 3.0.8 on 2020-08-04 20:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='immobilien',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('photo', models.ImageField(upload_to='photos/sellers')),
                ('description', models.TextField(blank=True)),
                ('email', models.CharField(max_length=25)),
                ('phone', models.CharField(max_length=70)),
                ('topseller', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date_time_joined')),
            ],
        ),
    ]
