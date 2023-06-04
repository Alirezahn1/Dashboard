from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
 path('income', views.index, name="income"),
 path('add-income', views.add_income, name="add-income"),
 path('edit-income/<int:id>', views.income_edit, name="income-edit"),
 path('income-delete/<int:id>', views.delete_income, name="income-delete"),
 path('search-income', csrf_exempt(views.search_income),
      name="search_income"),
path('income_source_summary', views.income_source_summary,
      name="income_source_summary"),
    path('stats2', views.stats_view,
         name="stats2"),
    path('export-csv2', views.export_csv,
         name="export-csv2")

]