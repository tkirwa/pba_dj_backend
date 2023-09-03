# Generated by Django 4.2.4 on 2023-09-03 17:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("api", "0010_alter_setting_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="income",
            name="category",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="incomes",
                to="api.incomecategory",
            ),
        ),
        migrations.AlterField(
            model_name="income",
            name="user",
            field=models.ForeignKey(
                default=1,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="incomes",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]