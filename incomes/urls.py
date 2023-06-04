from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
 path('income', views.index, name="income"),
 path('add-income', views.add_income, name="add-income"),
 # path('edit-expense/<int:id>', views.expense_edit, name="expense-edit"),
 # path('expense-delete/<int:id>', views.delete_expense, name="expense-delete"),
 # path('search-expenses', csrf_exempt(views.search_expenses),
 #      name="search_expenses"),

]