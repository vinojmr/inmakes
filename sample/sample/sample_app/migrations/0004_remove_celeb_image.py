# Generated by Django 4.1.4 on 2023-03-30 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("sample_app", "0003_alter_celeb_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="celeb",
            name="image",
        ),
    ]
