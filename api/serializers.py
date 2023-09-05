from rest_framework import serializers
from .models import Expense, ExpenseCategory, Income, IncomeCategory
from .models import Setting
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
    category = serializers.CharField(source='category.name')

    class Meta:
        model = Expense
        fields = ('id', 'name', 'category', 'amount', 'date')


# IncomeCategorySerializer and IncomeSerializer
class IncomeCategorySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = IncomeCategory
        fields = '__all__'


class IncomeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Income
        fields = '__all__'


# Settings Serializer
class SettingsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Setting
        fields = '__all__'
