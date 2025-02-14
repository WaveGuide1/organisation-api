# Generated by Django 5.0.6 on 2024-07-06 01:42

import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("organisation", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="organisation",
            name="users",
            field=models.ManyToManyField(
                related_name="organisations", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="organisation",
            name="description",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="organisation",
            name="name",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="organisation",
            name="orgId",
            field=models.UUIDField(
                default=uuid.uuid4,
                editable=False,
                primary_key=True,
                serialize=False,
                unique=True,
            ),
        ),
    ]
