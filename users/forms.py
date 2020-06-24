from django import forms
import re
from .models import User


class FacultyCreationForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Your First Name Here",
                   "class": "form-control"}))
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Your Last Name Here",
                   "class": "form-control"}))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={"placeholder": "Your Email Here",
                   "class": "form-control"}))

    password1 = forms.CharField(
        label=("Password"),
        widget=forms.PasswordInput(attrs={
            "placeholder": "Your Password Here",
            "class": "form-control"}))

    password2 = forms.CharField(
        label=("Password confirmation"),
        widget=forms.PasswordInput(
            attrs={"placeholder": "Confirm Your Password Here",
                   "class": "form-control"}),
        help_text=("Enter the same password as above, for verification."))

    phone_no = forms.CharField(
        widget=forms.NumberInput(
            attrs={"placeholder": "Your Phone No. Here",
                   "class": "form-control"}))

    registration_no = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Verify Registration Here",
                   "class": "form-control"}))

    address = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Your address",
                "class": "form-control",
                "rows": 5, }))

    department = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Department Here",
                   "class": "form-control"}))

    user_photo = forms.ImageField(widget=forms.FileInput(
        attrs={"class": "form-control",
               "accept": "image/*"}))

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "registration_no",
                  "phone_no", "password1", "password2",
                  "address", "department", "user_photo")

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("The password did not match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_faculty = True
        user.set_password(self.cleaned_data["password1"])

        if commit:
            user.save()
        return user


class StudentCreationForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Your First Name Here",
                   "class": "form-control"}))
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Your Last Name Here",
                   "class": "form-control"}))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={"placeholder": "Your Email Here",
                   "class": "form-control"}))

    password1 = forms.CharField(
        label=("Password"),
        widget=forms.PasswordInput(attrs={
            "placeholder": "Your Password Here",
            "class": "form-control"}))

    password2 = forms.CharField(
        label=("Password confirmation"),
        widget=forms.PasswordInput(
            attrs={"placeholder": "Confirm Your Password Here",
                   "class": "form-control"}),
        help_text=("Enter the same password as above, for verification."))

    phone_no = forms.CharField(
        widget=forms.NumberInput(
            attrs={"placeholder": "Your Phone No. Here",
                   "class": "form-control"}))

    registration_no = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Verify Registration Here",
                   "class": "form-control"}))

    address = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Your address",
                "class": "form-control",
                "rows": 5, }))

    department = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Department Here",
                   "class": "form-control"}))

    course = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Course Here",
                   "class": "form-control"}))

    group = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Group Here",
                   "class": "form-control"}))

    user_photo = forms.ImageField(widget=forms.FileInput(
        attrs={"class": "form-control",
               "accept": "image/*"}))

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "registration_no",
                  "phone_no", "password1", "password2",
                  "address", "department", "course", "group", "user_photo")

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("The password did not match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_student = True
        user.set_password(self.cleaned_data["password1"])

        if commit:
            user.save()
        return user
