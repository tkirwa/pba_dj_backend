from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# from django.conf import settings


# Expense Category & Model
class ExpenseCategory(models.Model):
    class Meta:
        verbose_name_plural = "Expense Categories"

    name = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Expense(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(ExpenseCategory, related_name='expenses',
                                 on_delete=models.SET_NULL,
                                 null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    date = models.DateTimeField(default=timezone.now)

    user = models.ForeignKey(User,
                             on_delete=models.SET_NULL, null=True,
                             default=1)

    def __str__(self):
        return self.name


# Income Category & Model
class IncomeCategory(models.Model):
    class Meta:
        verbose_name_plural = " Income Categories"

    name = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Income(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(IncomeCategory, related_name='expenses',
                                 on_delete=models.SET_NULL,
                                 null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User,
                             on_delete=models.SET_NULL, null=True,
                             default=1)

    def __str__(self):
        return self.name


# User settings - currency_preference and timezone
class Setting(models.Model):
    # name = models.CharField(max_length=100)
    user = models.OneToOneField(User, related_name='settings',
                                on_delete=models.CASCADE, null=True,
                                default=1)
    currency_preference = models.CharField(max_length=100,
                                           default='Kenyan Shilling (KES)')
    timezone = models.CharField(max_length=100,
                                default='Eastern Time Zone (ET)')
