# Generated by Django 4.2 on 2023-04-17 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("webpages", "0002_slider_photo_alter_slider_button_text"),
    ]

    operations = [
        migrations.CreateModel(
            name="team",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("firstname", models.CharField(max_length=100)),
                ("lastname", models.CharField(max_length=100)),
                ("role", models.CharField(max_length=100)),
                ("fblink", models.CharField(max_length=100)),
                ("instalink", models.CharField(max_length=100)),
                ("photo", models.ImageField(upload_to="media/team/%Y/%m/%d/")),
                ("created_date", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]