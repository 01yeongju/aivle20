# Generated by Django 4.2 on 2023-12-29 06:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("safetydetects", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="AIAnalysisResult",
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
                ("processed_image", models.ImageField(upload_to="processed_image/")),
                ("analysis_text", models.TextField()),
                (
                    "original_image",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="safetydetects.uploadedimage",
                    ),
                ),
            ],
            options={
                "db_table": "ai_analysis",
            },
        ),
    ]
