# Generated by Django 3.2.12 on 2022-04-03 19:58

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0014_auto_20220403_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='price_with_legi',
            field=models.DecimalField(blank=True, decimal_places=2, default=Decimal('35'), max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='price_without_legi',
            field=models.DecimalField(blank=True, decimal_places=2, default=Decimal('70'), max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='pricereduction',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='subscribe',
            name='price_to_pay',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='teach',
            name='hourly_wage',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Hourly wage, leave empty to copy default wage from teacher profile.', max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='teachlesson',
            name='hourly_wage',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Hourly wage, leave empty to copy default wage from teacher profile.', max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='default_hourly_wage',
            field=models.DecimalField(decimal_places=2, default=Decimal('30'), help_text='The default hourly wage, which serves as a preset value for taught courses. ', max_digits=6),
        ),
    ]
