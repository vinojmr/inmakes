# Generated by Django 4.1.4 on 2023-03-08 07:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app0", "0005_rename_travello_place_rename_description_place_desc_and_more"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Place",
            new_name="Travel",
        ),
    ]