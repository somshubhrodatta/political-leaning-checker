# Generated by Django 5.1.2 on 2025-07-22 16:14

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="UserResponse",
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
                ("question_1", models.IntegerField()),
                ("question_2", models.IntegerField()),
                ("question_3", models.IntegerField()),
                ("question_4", models.IntegerField()),
                ("question_5", models.IntegerField()),
                ("question_6", models.IntegerField()),
                ("question_7", models.IntegerField()),
                ("question_8", models.IntegerField()),
                ("question_9", models.IntegerField()),
                ("question_10", models.IntegerField()),
                ("score", models.FloatField()),
                ("label", models.CharField(max_length=20)),
                ("comparison", models.TextField()),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
