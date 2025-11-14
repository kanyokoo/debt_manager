from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_debtor_view, name='add_debtor'),
    path('debtor/<int:pk>/', views.debtor_detail_view, name='debtor_detail'),
    path('debtor/<int:pk>/add_debt/', views.add_debt_view, name='add_debt'),
    path('debtor/<int:pk>/delete/', views.delete_debtor_view, name='delete_debtor'),
]
