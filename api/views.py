# apis/views.py
from rest_framework import generics

from rest_framework.generics import RetrieveAPIView
from django.contrib.auth.models import User
from .serializers import UserSerializer

from api.permissions import IsOwnerOrReadOnly, IsOwnerAndAuthenticated
from rest_framework.permissions import IsAuthenticated

from knox.auth import TokenAuthentication

from .models import Expense, Income, ExpenseCategory, IncomeCategory
from .models import Setting
from .serializers import ExpenseSerializer, IncomeSerializer
from .serializers import ExpenseCategorySerializer, IncomeCategorySerializer
from .serializers import SettingsSerializer


class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Create, List, Retrieve and Destroy Expense
class ListCreateExpense(generics.ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        # Filter expenses by the currently authenticated user
        return Expense.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Set the user field to the currently authenticated user
        serializer.save(user=self.request.user)


class DetailExpense(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    # permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]


# Create, List, Retrieve and Destroy Expense Categories
class ListExpenseCategory(generics.ListCreateAPIView):
    queryset = ExpenseCategory.objects.all()
    serializer_class = ExpenseCategorySerializer
    # permission_classes = [IsAuthenticated]


class DetailExpenseCategory(generics.RetrieveUpdateDestroyAPIView):
    queryset = ExpenseCategory.objects.all()
    serializer_class = ExpenseCategorySerializer
    # permission_classes = [IsAuthenticated]


# Create, List, Retrieve and Destroy Income
class ListCreateIncome(generics.ListCreateAPIView):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
    permission_classes = [IsOwnerOrReadOnly]
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        return Income.objects.filter(user=self.request.user)


class DetailIncome(generics.RetrieveUpdateDestroyAPIView):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
    # permission_classes = [IsOwnerOrReadOnly, IsOwnerAndAuthenticated]
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]


# Create, List, Retrieve and Destroy Income Category
class ListIncomeCategory(generics.ListCreateAPIView):
    queryset = IncomeCategory.objects.all()
    serializer_class = IncomeCategorySerializer
    # permission_classes = [IsOwnerOrReadOnly, IsOwnerAndAuthenticated]

    # def get_queryset(self):
    #     user = self.request.user
    #     return IncomeCategory.objects.filter(user=user)


class DetailIncomeCategory(generics.RetrieveUpdateDestroyAPIView):
    queryset = IncomeCategory.objects.all()
    serializer_class = IncomeCategorySerializer


# Settings view
class ListSettingView(generics.ListCreateAPIView):
    queryset = Setting.objects.all()
    serializer_class = SettingsSerializer
    permission_classes = [IsOwnerOrReadOnly]
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        return Setting.objects.filter(user=self.request.user)


class DetailSettingView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Setting.objects.all()
    serializer_class = SettingsSerializer
