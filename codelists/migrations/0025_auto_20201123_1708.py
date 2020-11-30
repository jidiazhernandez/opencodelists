# Generated by Django 3.1.3 on 2020-11-23 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("codelists", "0024_codelistversion_discarded"),
    ]

    operations = [
        migrations.AlterField(
            model_name="codelist",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="codelist",
            name="methodology",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="codelist",
            name="name",
            field=models.CharField(max_length=255, verbose_name="Codelist name"),
        ),
    ]