# Generated by Django 2.2.10 on 2020-03-26 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post_office', '0008_attachment_headers'),
        ('survey', '0001_squashed_0011_auto_20190904_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='surveyinstance',
            name='email_template',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='survey_instances', to='post_office.EmailTemplate'),
        ),
    ]