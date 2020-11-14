# Generated by Django 3.1.3 on 2020-11-12 12:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("opencodelists", "0003_delete_project"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="organisation",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="opencodelists.organisation",
            ),
        ),
        migrations.CreateModel(
            name="Membership",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("is_admin", models.BooleanField(default=False)),
                ("date_joined", models.DateField()),
                (
                    "organisation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="memberships",
                        to="opencodelists.organisation",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="memberships",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "unique_together": {("user", "organisation")},
            },
        ),
        migrations.AddField(
            model_name="organisation",
            name="users",
            field=models.ManyToManyField(
                related_name="organisations",
                through="opencodelists.Membership",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
