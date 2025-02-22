# Generated by Django 5.1.2 on 2024-12-29 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="talent",
            name="area",
        ),
        migrations.AddField(
            model_name="consultant",
            name="age",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name="consultant",
            name="awards",
            field=models.JSONField(blank=True, default=list),
        ),
        migrations.AddField(
            model_name="consultant",
            name="education_details",
            field=models.JSONField(blank=True, default=list),
        ),
        migrations.AddField(
            model_name="consultant",
            name="education_level",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name="consultant",
            name="experience",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name="consultant",
            name="experience_details",
            field=models.JSONField(blank=True, default=list),
        ),
        migrations.AddField(
            model_name="consultant",
            name="language",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="talent",
            name="age",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name="talent",
            name="awards",
            field=models.JSONField(blank=True, default=list),
        ),
        migrations.AddField(
            model_name="talent",
            name="education_details",
            field=models.JSONField(blank=True, default=list),
        ),
        migrations.AddField(
            model_name="talent",
            name="education_level",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name="talent",
            name="experience",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name="talent",
            name="experience_details",
            field=models.JSONField(blank=True, default=list),
        ),
        migrations.AddField(
            model_name="talent",
            name="language",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="consultant",
            name="photo",
            field=models.ImageField(
                blank=True, default="", null=True, upload_to="consultants/photos/"
            ),
        ),
        migrations.AlterField(
            model_name="talent",
            name="photo",
            field=models.ImageField(
                blank=True, default="", null=True, upload_to="talent/photos/"
            ),
        ),
    ]
