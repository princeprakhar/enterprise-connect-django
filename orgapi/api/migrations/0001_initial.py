# Generated by Django 5.1.2 on 2024-11-02 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Company",
            fields=[
                ("company_id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=30)),
                ("company", models.CharField(max_length=30)),
                ("location", models.CharField(max_length=30)),
                ("about", models.TextField()),
                (
                    "type",
                    models.CharField(
                        choices=[("public", "Public"), ("private", "Private")],
                        max_length=30,
                    ),
                ),
                ("date", models.DateTimeField(auto_now_add=True)),
                ("active", models.BooleanField(default=True)),
            ],
        ),
    ]