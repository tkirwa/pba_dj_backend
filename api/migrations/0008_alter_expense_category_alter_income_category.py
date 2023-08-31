# Generated by Django 4.2.4 on 2023-08-31 08:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0007_alter_expense_user_alter_income_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="expense",
            name="category",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="expenses",
                to="api.expensecategory",
            ),
        ),
        migrations.AlterField(
            model_name="income",
            name="category",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="expenses",
                to="api.incomecategory",
            ),
        ),
    ]