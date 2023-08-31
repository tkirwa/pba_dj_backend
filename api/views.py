# apis/views.py
from rest_framework import generics

from rest_framework.generics import RetrieveAPIView
from django.contrib.auth.models import User
from .serializers import UserSerializer

from .models import Expense, Income, ExpenseCategory, IncomeCategory
from .serializers import ExpenseSerializer, IncomeSerializer
from .serializers import ExpenseCategorySerializer, IncomeCategorySerializer


class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Create, List, Retrieve and Destroy Expense
class ListExpense(generics.ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer


class DetailExpense(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer


# Create, List, Retrieve and Destroy Expense Categories
class ListExpenseCategory(generics.ListCreateAPIView):
    queryset = ExpenseCategory.objects.all()
    serializer_class = ExpenseCategorySerializer


class DetailExpenseCategory(generics.RetrieveUpdateDestroyAPIView):
    queryset = ExpenseCategory.objects.all()
    serializer_class = ExpenseCategorySerializer


# Create, List, Retrieve and Destroy Income
class ListIncome(generics.ListCreateAPIView):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer


class DetailIncome(generics.RetrieveUpdateDestroyAPIView):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer


# Create, List, Retrieve and Destroy Income Category
class ListIncomeCategory(generics.ListCreateAPIView):
    queryset = IncomeCategory.objects.all()
    serializer_class = IncomeCategorySerializer


class DetailIncomeCategory(generics.RetrieveUpdateDestroyAPIView):
    queryset = IncomeCategory.objects.all()
    serializer_class = IncomeCategorySerializer
