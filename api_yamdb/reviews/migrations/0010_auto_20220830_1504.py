# Generated by Django 2.2.16 on 2022-08-30 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0009_merge_20220830_1422"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="pub_date",
            field=models.DateTimeField(
                auto_now_add=True, verbose_name="Дата публикации"
            ),
        ),
        migrations.AlterUniqueTogether(
            name="review",
            unique_together=set(),
        ),
    ]
