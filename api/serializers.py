from rest_framework import serializers
from .models import Expense, ExpenseCategory, Income, IncomeCategory
from django.contrib.auth.models import User

from rest_framework import serializers


# UserSerializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


# ExpenseCategorySerializer and ExpenseSerializer
class ExpenseCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ExpenseCategory
        fields = '__all__'


class ExpenseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'


# IncomeCategorySerializer and IncomeSerializer
class IncomeCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = IncomeCategory
        fields = '__all__'


class IncomeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Income
        fields = '__all__'
