# Generated by Django 5.1.2 on 2024-12-30 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0005_alter_consultant_language_alter_talent_language"),
    ]

    operations = [
        migrations.AddField(
            model_name="talent",
            name="area",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
