from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from saleboard.models import User


class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2',
        )
