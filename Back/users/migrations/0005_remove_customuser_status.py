# Generated by Django 5.1 on 2024-10-04 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_customuser_status"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customuser",
            name="status",
        ),
    ]
