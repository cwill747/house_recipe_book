# Generated by Django 4.0.3 on 2022-04-14 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_alter_profile_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="image",
            field=models.ImageField(default="default.jpg", upload_to="profile_pics"),
        ),
    ]
