# Generated by Django 4.2 on 2023-05-02 10:38

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_rename_user_userdata"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userdata",
            name="mail",
        ),
    ]
