# Generated by Django 4.2 on 2023-04-17 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("webpages", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="slider",
            name="photo",
            field=models.ImageField(null=True, upload_to="media/slider/%Y/"),
        ),
        migrations.AlterField(
            model_name="slider",
            name="button_text",
            field=models.CharField(max_length=255),
        ),
    ]
