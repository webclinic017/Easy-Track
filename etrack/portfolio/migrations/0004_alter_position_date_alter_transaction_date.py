# Generated by Django 4.0.1 on 2022-02-07 13:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_position_date_transaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 2, 7, 8, 22, 45, 747541)),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 2, 7, 8, 22, 45, 747541)),
        ),
    ]
