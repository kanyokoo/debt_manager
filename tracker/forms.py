from django import forms
from .models import Debtor
from .models import Debtor, Payment


class DebtorForm(forms.ModelForm):
    class Meta:
        model = Debtor
        # These are the fields the user will see and fill out
        fields = ['name', 'initial_amount', 'description']
        
        # Optional: Add Bootstrap classes to the form fields for better styling
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'initial_amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }



class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['amount']
        widgets = {
            'amount': forms.NumberInput(attrs={'class': 'form-control'})
        }
    def clean_amount(self):
        # Get the value submitted by the user
        amount = self.cleaned_data.get('amount')
        
        # Check if the amount is less than or equal to zero
        if amount <= 0:
            # If it is, raise a validation error. Django will show this to the user.
            raise forms.ValidationError("The payment amount must be greater than zero.")
            
        # If the validation passes, always return the cleaned data
        return amount

class AddDebtForm(forms.Form):
    amount = forms.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    description = forms.CharField(
        required=False, 
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3})
    )
