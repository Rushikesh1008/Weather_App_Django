from django.forms import ModelForm, TextInput
from django import forms
from .models import City,Feedback,Contact
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,get_user_model

User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self,*args,**kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username = username, password = password)
            if not user:
                raise forms.ValidationError("Please check the credintials.")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect password.")
            if not user.is_active:
                raise forms.ValidationError("This user is not active.")
        return super(UserLoginForm, self).clean(*args,*kwargs)

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("This email is already being used.")
        return email

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
