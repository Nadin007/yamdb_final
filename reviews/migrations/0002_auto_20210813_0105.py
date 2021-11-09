# Generated by Django 2.2.6 on 2021-08-13 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0001_initial"),
    ]

    operations = [
        migrations.AddConstraint(
            model_name="user",
            constraint=models.CheckConstraint(
                check=models.Q(_negated=True, username="me"),
                name="User_can_not_be_name_me",
            ),
        ),
    ]
