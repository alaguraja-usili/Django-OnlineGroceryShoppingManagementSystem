# Generated by Django 3.0.5 on 2021-11-28 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bazaar', '0008_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='mobile',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
