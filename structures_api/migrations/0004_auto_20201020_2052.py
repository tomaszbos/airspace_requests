# Generated by Django 3.1.2 on 2020-10-20 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('structures_api', '0003_auto_20201019_2011'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reservation',
            options={'permissions': [('request_tsa', 'Can request TSA type airspace'), ('request_tra', 'Can request TRA type airspace'), ('request_ea', 'Can request EA type airspace'), ('request_atz', 'Can request ATZ type airspace'), ('request_mrt', 'Can request MRT type airspace')]},
        ),
        migrations.AlterField(
            model_name='airspacestructure',
            name='airspace_type',
            field=models.CharField(choices=[('TSA', 'TSA'), ('TRA', 'TRA'), ('EA', 'EA'), ('D', 'D'), ('R', 'R'), ('P', 'P'), ('CTR', 'CTR'), ('TMA', 'TMA'), ('ATZ', 'ATZ'), ('MCTR', 'MCTR'), ('ADIZ', 'ADIZ'), ('MTMA', 'MTMA'), ('MRT', 'MRT')], max_length=5),
        ),
    ]
