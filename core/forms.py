
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class UserCreateForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'username', "bio", "phone", "address"]



