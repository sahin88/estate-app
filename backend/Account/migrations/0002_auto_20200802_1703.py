# Generated by Django 3.0.5 on 2020-08-02 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='is_stuff',
            new_name='is_staff',
        ),
    ]
