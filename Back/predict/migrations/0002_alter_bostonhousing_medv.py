# Generated by Django 5.1 on 2024-09-23 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("predict", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bostonhousing",
            name="medv",
            field=models.FloatField(blank=True, null=True),
        ),
    ]
