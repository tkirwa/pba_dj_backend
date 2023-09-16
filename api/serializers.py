from rest_framework import serializers
from .models import Expense, ExpenseCategory, Income, IncomeCategory
from .models import Setting
from django.contrib.auth.models import User

from rest_framework import serializers

from rest_framework import status
from rest_framework.response import Response


# UserSerializer
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


# ExpenseCategorySerializer and ExpenseSerializer
class ExpenseCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ExpenseCategory
        fields = '__all__'


class ExpenseSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.CharField()
    # user = serializers.CharField()

    class Meta:
        model = Expense
        fields = ('url', 'id', 'name', 'category', 'amount', 'date', 'user')

    def create(self, validated_data):
        # Extract the category_name from the validated data
        category = validated_data.pop('category', None)

        # Create or retrieve the ExpenseCategory instance based on the name
        if category:
            category, _ = ExpenseCategory.objects.get_or_create(name=category)
            validated_data['category'] = category

        # Automatically set the authenticated user as the "user" field
        validated_data['user'] = self.context['request'].user

        # Create the Expense instance
        expense = Expense.objects.create(**validated_data)

        return expense

    def update(self, instance, validated_data):
        # Update the instance with the validated data
        instance.name = validated_data.get('name', instance.name)
        instance.amount = validated_data.get('amount', instance.amount)
        instance.date = validated_data.get('date', instance.date)

        # Retrieve or create the ExpenseCategory instance
        category_data = validated_data.get('category')
        category, _ = ExpenseCategory.objects.get_or_create(name=category_data)
        instance.category = category

        # Save the instance
        instance.save()

        return instance


# IncomeCategorySerializer and IncomeSerializer
class IncomeCategorySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = IncomeCategory
        fields = '__all__'


class IncomeSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.CharField()
    # user = serializers.CharField()

    class Meta:
        model = Income
        fields = ('url', 'id', 'name', 'category', 'amount', 'date', 'user')

    def create(self, validated_data):
        # Extract the category_name from the validated data
        category = validated_data.pop('category', None)

        # Create or retrieve the IncomeCategory instance based on the name
        if category:
            category, _ = IncomeCategory.objects.get_or_create(name=category)
            validated_data['category'] = category

        # Automatically set the authenticated user as the "user" field
        validated_data['user'] = self.context['request'].user

        # Create the Income instance
        income = Income.objects.create(**validated_data)

        return income

    def update(self, instance, validated_data):
        # Update the instance with the validated data
        instance.name = validated_data.get('name', instance.name)
        instance.amount = validated_data.get('amount', instance.amount)
        instance.date = validated_data.get('date', instance.date)

        # Retrieve or create the ExpenseCategory instance
        category_data = validated_data.get('category')
        category, _ = IncomeCategory.objects.get_or_create(name=category_data)
        instance.category = category

        # Save the instance
        instance.save()

        return instance


# Settings Serializer
class SettingsSerializer(serializers.HyperlinkedModelSerializer):
    # Use the UserSerializer to display user information
    user = UserSerializer()

    class Meta:
        model = Setting
        # fields = '__all__'
        fields = ('url', 'id', 'currency_preference', 'timezone', 'user')
