# Generated by Django 3.1.2 on 2020-10-18 14:20

from django.db import migrations, models
import structures_api.validators


class Migration(migrations.Migration):

    dependencies = [
        ('structures_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='activation_time',
            field=models.DateTimeField(validators=[structures_api.validators.reservation_validator_since]),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='deactivation_time',
            field=models.DateTimeField(validators=[structures_api.validators.reservation_validator_to]),
        ),
    ]
