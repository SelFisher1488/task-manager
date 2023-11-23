# Generated by Django 4.2.7 on 2023-11-23 00:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tasks", "0003_alter_task_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="priority",
            field=models.CharField(
                choices=[
                    ("Urgent", "1"),
                    ("High", "2"),
                    ("Medium", "3"),
                    ("Low", "4"),
                    ("Optional", "Optional"),
                ],
                default="low",
                max_length=255,
            ),
        ),
    ]