# Generated by Django 4.1.2 on 2022-11-16 13:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("notes", "0013_checkvotes_delete_upvotes"),
    ]

    operations = [
        migrations.AddField(
            model_name="notes",
            name="details",
            field=models.CharField(default="", max_length=500),
        ),
        migrations.AlterField(
            model_name="notes",
            name="description",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.CreateModel(
            name="Comments",
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
                ("cmnt", models.CharField(max_length=200)),
                ("dates", models.CharField(max_length=30)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
