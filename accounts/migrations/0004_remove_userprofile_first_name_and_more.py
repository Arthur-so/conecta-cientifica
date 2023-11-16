# Generated by Django 4.2.4 on 2023-11-08 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_education_researcharea_researchproject_tag_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userprofile",
            name="first_name",
        ),
        migrations.RemoveField(
            model_name="userprofile",
            name="last_name",
        ),
        migrations.AddField(
            model_name="education",
            name="degree",
            field=models.CharField(default="Graduação", max_length=100),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="name",
            field=models.CharField(default="", max_length=100),
        ),
    ]