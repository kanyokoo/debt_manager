# accounts/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Required. A valid email address.')

    class Meta(UserCreationForm.Meta):
        model = User
        # --- THIS IS THE CORRECTED LINE ---
        # We only list the fields that the Meta class should handle directly.
        # The password fields are added automatically by the parent UserCreationForm.
        fields = ("username", "email")

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("An account with this email address already exists.")
        return email
