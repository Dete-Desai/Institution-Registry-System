from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model

)
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
User = get_user_model()

# Create your form functions here

#AUTHENTICATION
ACCOUNT_CHOICES= [
    ('viewer', 'Institution Viewer'),
    ]

#Registration
class CreateUserForm(UserCreationForm):
    account_type = forms.CharField(label='Account Type:', widget=forms.Select(choices=ACCOUNT_CHOICES))

    class Meta:
        model = User
        fields = ['username','email','account_type','password1','password2']

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields['account_type'].empty_label = '--Choose Account--'