# Generated by Django 3.0.8 on 2020-08-14 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packs', '0010_auto_20200814_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pack',
            name='publish_date',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]