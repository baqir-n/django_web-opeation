from django import forms
from .models import Employee,User

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('uemail', 'password')

class PasswordForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('password', 'repassword' )
