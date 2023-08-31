from django.urls import path
from . import views
from .views import UserDetailView


urlpatterns = [

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


# # apis/urls.py
# from django.urls import path

# from .views import ListExpense, DetailExpense
# from .views import ListExpenseCategory, DetailExpenseCategory
# from .views import ListIncome, DetailIncome
# from .views import ListIncomeCategory, DetailIncomeCategory

# urlpatterns = [

#     # Expenses and Expense Categories Paths
#     path('expenses', ListExpense.as_view(), name='expense-list'),
#     path('expense/<int:pk>/', DetailExpense.as_view(),
# name='expense-detail'),
#     path('expense-categories', ListExpenseCategory.as_view(),
#          name='expensecategory-list'),
#     path('expense-categories/<int:pk>/', DetailExpenseCategory
#          .as_view(), name='expensecategory-detail'),


#     # Income and Income Categories Paths
#     path('incomes', ListIncome.as_view(), name='income-list'),
#     path('income/<int:pk>/', DetailIncome.as_view(), name='income-detail'),
#     path('income-categories', ListIncomeCategory.as_view(),
#          name='incomecategory-list'),
#     path('income-categories/<int:pk>/', DetailIncomeCategory.as_view(),
#          name='incomecategory-detail'),
# ]
