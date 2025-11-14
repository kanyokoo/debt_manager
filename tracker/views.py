# tracker/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages # Import the messages framework
from .forms import DebtorForm, PaymentForm, AddDebtForm
from .models import Debtor, Payment

# View to add a completely new debtor
@login_required
def add_debtor_view(request):
    if request.method == 'POST':
        form = DebtorForm(request.POST)
        if form.is_valid():
            debtor = form.save(commit=False)
            debtor.owner = request.user
            debtor.save()
            # Add a success message for the user
            messages.success(request, f'Successfully added "{debtor.name}" to your records.')
            return redirect('dashboard')
    else:
        form = DebtorForm()
        
    return render(request, 'tracker/add_debtor.html', {'form': form})

# View to see the details of a single debtor
@login_required
def debtor_detail_view(request, pk):
    debtor = get_object_or_404(Debtor, pk=pk, owner=request.user)
    
    # This part handles when the user submits the "Record Payment" form
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.debtor = debtor
            payment.save()
            # Add a success message for the user
            messages.success(request, f'Payment of Ksh. {payment.amount} recorded for "{debtor.name}".')
            return redirect('debtor_detail', pk=debtor.pk)
    else:
        # This part runs when the page is first loaded (a GET request)
        form = PaymentForm()

    payments = debtor.payments.all().order_by('-payment_date')
    balance = debtor.get_current_balance()

    context = {
        'debtor': debtor,
        'payments': payments,
        'balance': balance,
        'form': form
    }
    
    return render(request, 'tracker/debtor_detail.html', context)

# View to add MORE debt to an existing debtor
@login_required
def add_debt_view(request, pk):
    debtor = get_object_or_404(Debtor, pk=pk, owner=request.user)
    if request.method == 'POST':
        form = AddDebtForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            description = form.cleaned_data['description']
            
            # Create a new payment object with a NEGATIVE amount
            Payment.objects.create(
                debtor=debtor,
                amount=-amount
            )
            
            if description:
                debtor.description += f"\n- Debt Added: {description}"
                debtor.save()
            
            # Add a success message for the user
            messages.success(request, f'Added Ksh. {amount} to the debt for "{debtor.name}".')
            return redirect('debtor_detail', pk=debtor.pk)
    else:
        form = AddDebtForm()

    context = {
        'form': form,
        'debtor': debtor
    }
    return render(request, 'tracker/add_debt.html', context)

# View to delete a debtor
@login_required
def delete_debtor_view(request, pk):
    debtor = get_object_or_404(Debtor, pk=pk, owner=request.user)
    
    if request.method == 'POST':
        debtor_name = debtor.name # Store the name before deleting
        debtor.delete()
        # Add a success message for the user
        messages.success(request, f'The record for "{debtor_name}" has been successfully deleted.')
        return redirect('dashboard')
        
    context = {'debtor': debtor}
    return render(request, 'tracker/delete_debtor_confirm.html', context)
