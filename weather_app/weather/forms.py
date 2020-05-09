from django.forms import ModelForm, TextInput
from django import forms
from .models import City,Feedback,Contact

class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']

class feedback_form(ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Name'
        }
    ))
    email = forms.CharField(widget=forms.EmailInput(
        attrs={
            'class':'form-control',
            'placeholder':'Email'
        }
    ))
    message = forms.CharField(widget=forms.Textarea(
        attrs={
            'class':'form-control',
            'placeholder':'Message'
        }
    ))
    class Meta:
        model = Feedback
        fields = "__all__"

class contact_form(ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'First Name'
        }
    ))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Last Name'
        }
    ))
    email = forms.CharField(widget=forms.EmailInput(
        attrs={
            'class':'form-control',
            'placeholder':'Email'
        }
    ))
    phone = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Phone Number'
        }
    ))
    message = forms.CharField(widget=forms.Textarea(
        attrs={
            'class':'form-control',
            'placeholder':'Message',
            'rows':'5',
        }
    ))
    class Meta:
        model = Contact
        fields = "__all__"
