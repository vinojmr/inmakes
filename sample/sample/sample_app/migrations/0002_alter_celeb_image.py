# Generated by Django 4.1.4 on 2023-03-29 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sample_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="celeb",
            name="image",
            field=models.ImageField(upload_to="gallery"),
        ),
    ]
