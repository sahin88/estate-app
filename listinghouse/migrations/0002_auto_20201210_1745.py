# Generated by Django 3.1.4 on 2020-12-10 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listinghouse', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='house_type',
            field=models.CharField(choices=[('House', 'House'), ('Condo', 'Condo'), ('Townhouse', 'Townhouse')], default='House', max_length=100),
        ),
    ]
