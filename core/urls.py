# core/urls.py

from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView # <-- IMPORT THIS
from django.urls import reverse_lazy # <-- IMPORT THIS

urlpatterns = [
    # This now points to our new pages app to handle the landing page
    path('', include('pages.urls')),
    
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')), 
    path('accounts/', include('accounts.urls')), 
    path('tracker/', include('tracker.urls')),
]