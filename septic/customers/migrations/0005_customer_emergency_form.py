# Generated by Django 3.2.7 on 2021-09-23 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0004_auto_20210922_1911'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='emergency_form',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
