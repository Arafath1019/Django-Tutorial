from django import forms
from .models import Contact

# class ContactForm(forms.Form):
#     name = forms.CharField(max_length=100, label="You Name")
#     phone = forms.CharField(max_length=100, label="You Phone")
#     content = forms.CharField(max_length=100, label="Your Details")

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"