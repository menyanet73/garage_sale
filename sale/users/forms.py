from django import forms
from django.contrib.auth.forms import UserCreationForm
from saleboard.models import User
from .models import UserProfile


class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            'username',
        )


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = (
            'first_name',
            'last_name',
            'phone',
            'email',
            'avatar',
        )
