# Generated by Django 4.1.2 on 2022-11-03 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("notes", "0005_alter_signup_username"),
    ]

    operations = [
        migrations.AlterField(
            model_name="signup",
            name="username",
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
