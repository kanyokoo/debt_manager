# core/urls.py

from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView # <-- IMPORT THIS
from django.urls import reverse_lazy # <-- IMPORT THIS

urlpatterns = [
    # --- ADD THIS NEW PATH ---
    # This makes the root URL redirect to the login page
    path('', RedirectView.as_view(url=reverse_lazy('login'), permanent=False)),
    
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')), 
    path('accounts/', include('accounts.urls')), 
    path('tracker/', include('tracker.urls')),
]