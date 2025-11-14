from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal


# The main model for an individual who owes money
class Debtor(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    initial_amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    def get_current_balance(self):
        # Get all payments related to this debtor
        payments = self.payments.all()
        # Sum up the amount of all payments
        total_paid = sum(payment.amount for payment in payments)
        # Calculate the balance
        balance = self.initial_amount - total_paid
        return balance


# Model for each payment transaction made by a Debtor
class Payment(models.Model):
    debtor = models.ForeignKey(Debtor, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment of {self.amount} for {self.debtor.name}"
