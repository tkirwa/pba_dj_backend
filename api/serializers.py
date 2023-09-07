from rest_framework import serializers
from .models import Expense, ExpenseCategory, Income, IncomeCategory
from .models import Setting
from django.contrib.auth.models import User

from rest_framework import serializers


# UserSerializer
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ('url', 'id', 'username', 'email', 'first_name',
# 'last_name')


# ExpenseCategorySerializer and ExpenseSerializer
class ExpenseCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ExpenseCategory
        fields = '__all__'


# class ExpenseSerializer(serializers.ModelSerializer):
#     category = serializers.SerializerMethodField()

#     class Meta:
#         model = Expense
#         fields = ('url', 'name', 'amount', 'date', 'category', 'user')

#     def get_category_name(self, obj):
#         return obj.category.name if obj.category else None


class ExpenseSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.CharField(source='category.name')

    class Meta:
        model = Expense
        # fields = '__all__'

        fields = ('url', 'id', 'name', 'category', 'amount', 'date', 'user')

    # def create(self, validated_data):
    #     # Extract the category_name from validated_data
    #     category_name = validated_data.pop('category_name')

    #     # Find or create the ExpenseCategory based on the category_name
    #     category, created = ExpenseCategory.objects.get_or_create(
    #         name=category_name)

    #     # Create the Expense object with the category
    #     expense = Expense.objects.create(category=category, **validated_data)
    #     return expense


# IncomeCategorySerializer and IncomeSerializer
class IncomeCategorySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = IncomeCategory
        fields = '__all__'


class IncomeSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.CharField(source='category.name')

    class Meta:
        model = Income
        # fields = '__all__'
        fields = ('url', 'id', 'name', 'category', 'amount', 'date', 'user')


# Settings Serializer
class SettingsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Setting
        fields = '__all__'
