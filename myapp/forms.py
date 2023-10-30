# Create a form to handle the user input.
# This form will be used in the view to validate and save the data.


from django import forms
from myapp.models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['firstname', 'lastname', 'email', 'password','age']
