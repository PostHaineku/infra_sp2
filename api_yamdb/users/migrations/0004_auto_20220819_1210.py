# Generated by Django 2.2.16 on 2022-08-19 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_user_confirmation_code"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={
                "ordering": ["username"],
                "verbose_name": "user",
                "verbose_name_plural": "users",
            },
        ),
    ]
