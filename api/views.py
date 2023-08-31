# apis/views.py
from rest_framework import generics

from rest_framework.generics import RetrieveAPIView
from django.contrib.auth.models import User
from .serializers import UserSerializer

from api.permissions import IsOwnerOrReadOnly, IsOwnerAndAuthenticated

from .models import Expense, Income, ExpenseCategory, IncomeCategory
from .models import Setting
from .serializers import ExpenseSerializer, IncomeSerializer
from .serializers import ExpenseCategorySerializer, IncomeCategorySerializer
from .serializers import SettingsSerializer


class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Create, List, Retrieve and Destroy Expense
class ListExpense(generics.ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [IsOwnerOrReadOnly]  # Apply custom permission


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
    permission_classes = [IsOwnerOrReadOnly, IsOwnerAndAuthenticated]


class DetailIncome(generics.RetrieveUpdateDestroyAPIView):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
    permission_classes = [IsOwnerOrReadOnly, IsOwnerAndAuthenticated]


# Create, List, Retrieve and Destroy Income Category
class ListIncomeCategory(generics.ListCreateAPIView):
    queryset = IncomeCategory.objects.all()
    serializer_class = IncomeCategorySerializer
    permission_classes = [IsOwnerOrReadOnly, IsOwnerAndAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Expense.objects.filter(user=user)


class DetailIncomeCategory(generics.RetrieveUpdateDestroyAPIView):
    queryset = IncomeCategory.objects.all()
    serializer_class = IncomeCategorySerializer


# Settings view
class ListSettingView(generics.ListCreateAPIView):
    queryset = Setting.objects.all()
    serializer_class = SettingsSerializer
    permission_classes = [IsOwnerOrReadOnly, IsOwnerAndAuthenticated]


class DetailSettingView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Setting.objects.all()
    serializer_class = SettingsSerializer
