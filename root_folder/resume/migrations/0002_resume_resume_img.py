# Generated by Django 4.1.4 on 2022-12-31 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("resume", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="resume",
            name="resume_img",
            field=models.ImageField(
                null=True, upload_to="resume_images", verbose_name="Image"
            ),
        ),
    ]
