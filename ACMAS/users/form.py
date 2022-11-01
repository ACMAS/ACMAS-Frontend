from django.contrib.auth.forms import UserCreationForm
from user.models import User
from django import forms
from django.core.exceptions import ValidationError
from django.forms.fields import EmailField
from django.forms.forms import Form


# create the user registration form
# user can fills details in the fields
# from our site it can send the verification link
# user can receives the verification link on the email they received
class User(UserCreationForm):
    username = forms.CharField(label="username")
    email = forms.EmailField(label="email")
    password = forms.CharField(label="password", widget=forms.PasswordInput)

    # to check if we have username in database already or not
    def username_check(self):
        username = self.cleaned_data["username"].lower()  # django build in function cleaned_data
        new = User.objects.filter(username=username)
        if new.count():
            raise ValidationError("User Already Exist!")
        return username

    def email_check(self):
        email = self.cleaned_data["email"].lower()
        new = User.objects.filter(email=email)
        if new.count():
            raise ValidationError("Email Already Exist")
        return email

    # save the username and email
    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data["username"],
            self.cleaned_data["email"],
            self.cleaned_data["password"]
        )
        return user
