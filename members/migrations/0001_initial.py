# Generated by Django 5.0.1 on 2024-11-13 09:27

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TeamMember",
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
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("role", models.CharField(max_length=100)),
                ("bio", models.TextField(blank=True)),
                ("date_joined", models.DateField(auto_now_add=True)),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={
                "ordering": ["first_name", "last_name"],
            },
        ),
    ]
