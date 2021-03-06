# Generated by Django 3.0.8 on 2020-10-17 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20201017_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='default_county',
            field=models.CharField(blank=True, default=' ', max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='default_phone_number',
            field=models.CharField(blank=True, default=' ', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='default_post_code',
            field=models.CharField(blank=True, default=' ', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='default_street_address1',
            field=models.CharField(blank=True, default=' ', max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='default_town_or_city',
            field=models.CharField(blank=True, default=' ', max_length=40, null=True),
        ),
    ]
