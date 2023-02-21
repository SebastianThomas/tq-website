# Generated by Django 4.1.7 on 2023-02-21 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_alter_course_offering_alter_course_period'),
    ]

    operations = [
        migrations.AlterField(
            model_name='period',
            name='date_from',
            field=models.DateField(help_text='The start date of this period.'),
        ),
        migrations.AlterField(
            model_name='period',
            name='date_to',
            field=models.DateField(help_text='The end date of this period. Can be left empty.'),
        ),
    ]
