# Generated by Django 2.2.10 on 2020-03-26 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0002_surveyinstance_email_template'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questiongroup',
            name='survey',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='survey.Survey'),
        ),
    ]