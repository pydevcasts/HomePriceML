# Generated by Django 5.1 on 2024-10-15 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0006_customuser_username"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customuser",
            name="username",
        ),
    ]