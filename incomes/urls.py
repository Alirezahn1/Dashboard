from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
 path('income', views.index, name="income"),
 path('add-income', views.add_income, name="add-income"),
 path('edit-income/<int:id>', views.income_edit, name="income-edit"),
 path('income-delete/<int:id>', views.delete_income, name="income-delete"),
 # path('search-expenses', csrf_exempt(views.search_expenses),
 #      name="search_expenses"),

]