from django import forms
from .models import Contact, Need_Help


class ContactForm(forms.ModelForm):

    full_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Your Full Name Here",
                                      "class": "form-control"}))

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "Your Email Here",
                                       "class": "form-control"}))
    subject = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Your Subject Here",
                                      "class": "form-control"}))

    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Your Message Here",
                "class": "form-control",
                "id": "my-id-for-textarea",
                "rows": 10, }))

    class Meta:
        model = Contact
        fields = ("full_name", "email", "subject", "message",)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)


class NeedHelpForm(forms.ModelForm):

    full_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Your Full Name Here",
                                      "class": "form-control"}))
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "Your Email Here",
                                       "class": "form-control"}))

    subject = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Your Subject Here",
                                      "class": "form-control"}))

    problem = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Your Problem Here",
                "class": "form-control",
                "id": "my-id-for-textarea",
                "rows": 10, }))

    class Meta:
        model = Need_Help
        fields = ("full_name", "email", "subject", "problem",)

    def __init__(self, *args, **kwargs):
        super(NeedHelpForm, self).__init__(*args, **kwargs)
