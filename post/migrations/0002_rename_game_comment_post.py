# Generated by Django 4.2.1 on 2023-05-25 11:41

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("post", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comment",
            old_name="game",
            new_name="post",
        ),
    ]
