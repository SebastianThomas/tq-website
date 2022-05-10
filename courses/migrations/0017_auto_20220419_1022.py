# Generated by Django 3.2.13 on 2022-04-19 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0016_alter_subscribe_usi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribe',
            name='state',
            field=models.CharField(choices=[('new', 'new'), ('confirmed', 'confirmed (to pay)'), ('payed', 'paid'),
                                            ('completed', 'completed'), ('rejected', 'rejected'),
                                            ('to_reimburse', 'to reimburse')],
                                   db_index=True, default='new', max_length=30),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.RunSQL("UPDATE courses_userprofile SET gender = 'man' WHERE gender = 'm'"),
        migrations.RunSQL("UPDATE courses_userprofile SET gender = 'woman' WHERE gender = 'w'"),
    ]