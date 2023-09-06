from django.contrib import admin

from .models import Expense, ExpenseCategory, Income, IncomeCategory
from .models import Setting

# Customize Django Admin
admin.site.site_header = "PBA :: Budget System"
admin.site.site_title = "Admin Panel"
admin.site.index_title = "PBA :: Budget System"


# Expense & ExpenseCategory
@admin.register(ExpenseCategory)
class ExpenseCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "date")


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "amount", "date", "user")
    search_fields = ("name",)


# Income & IncomeCategory
@admin.register(IncomeCategory)
class IncomeCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "date")


@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "amount", "date")
    search_fields = ("name",)


# Settings
@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
    list_display = ("user", "currency_preference", "timezone")
