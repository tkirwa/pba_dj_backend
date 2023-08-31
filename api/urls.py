from django.urls import path
from . import views
from .views import UserDetailView, ListSettingView, DetailSettingView


urlpatterns = [
    # List and create settings
    path('settings/', ListSettingView.as_view(), name='list-settings'),

    # Retrieve, update, and delete a specific setting
    path('settings/<int:pk>/', DetailSettingView.as_view(),
         name='setting-detail'),

    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    # Expenses and Expense Categories Paths
    path('expense-categories/', views.ListExpenseCategory.as_view(),
         name='expensecategory-list'),
    path('expense-categories/<int:pk>/', views.DetailExpenseCategory.as_view(),
         name='expensecategory-detail'),
    path('expenses/', views.ListExpense.as_view(),
         name='expense-list'),
    path('expenses/<int:pk>/', views.DetailExpense.as_view(),
         name='expense-detail'),

    # Income and Income Categories Paths
    path('income-categories/', views.ListIncomeCategory.as_view(),
         name='incomecategory-list'),
    path('income-categories/<int:pk>/', views.DetailIncomeCategory.as_view(),
         name='incomecategory-detail'),
    path('incomes/', views.ListIncome.as_view(), name='income-list'),
    path('incomes/<int:pk>/', views.DetailIncome.as_view(),
         name='income-detail'),
]
