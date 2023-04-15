# Generated by Django 4.1.7 on 2023-04-15 10:55

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("organization", "0008_alter_organization_founded"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserProfile",
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
                ("title", models.CharField(max_length=200)),
                ("logo", models.ImageField(blank=True, upload_to="uploads")),
                ("vision", models.CharField(blank=True, max_length=250)),
                ("mission", models.CharField(blank=True, max_length=500)),
                ("num_employees", models.CharField(max_length=20)),
                (
                    "founded",
                    models.PositiveIntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(1000),
                            django.core.validators.MaxValueValidator(2023),
                        ]
                    ),
                ),
                ("email", models.EmailField(max_length=255)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="survey",
            name="organization",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="organization.userprofile",
            ),
        ),
        migrations.DeleteModel(
            name="Organization",
        ),
    ]
