# accounts/views.py

from django.shortcuts import render, redirect
# REMOVE the old form import: from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from tracker.models import Debtor

# --- IMPORT OUR NEW CUSTOM FORM ---
from .forms import CustomUserCreationForm

def register_view(request):
    if request.method == 'POST':
        # --- USE THE NEW FORM ---
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        # --- USE THE NEW FORM ---
        form = CustomUserCreationForm()
    
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def dashboard_view(request):
    debtors_list = Debtor.objects.filter(owner=request.user).order_by('-created_at')
    search_query = request.GET.get('q')
    if search_query:
        debtors_list = debtors_list.filter(name__icontains=search_query)
    context = {
        'debtors': debtors_list
    }
    return render(request, 'accounts/dashboard.html', context)
