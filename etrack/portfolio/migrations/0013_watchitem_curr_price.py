# Generated by Django 4.0.1 on 2022-02-10 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0012_portfolio_total_deposits_alter_portfolio_balance_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchitem',
            name='curr_price',
            field=models.FloatField(default=0),
        ),
    ]