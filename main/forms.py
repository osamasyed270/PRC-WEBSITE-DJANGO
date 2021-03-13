from django import forms
from django.forms import ModelForm
from .models import Match_1_Register

class RegistrationForm(ModelForm):
    class Meta:
        model = Match_1_Register
        fields = ['image', 'full_name', 'email', 'mobile_no', 'name_in_game', 'game_id', 'age', 'gender', 'facebook_name']

        widgets = {
			'image': forms.FileInput(attrs={'class': 'default-btn', 'hidden': 'True', 'required': 'True'}),
			'full_name': forms.TextInput(attrs={'id': 'full_name', 'placeholder': 'Full Name'}),
			'email': forms.EmailInput(attrs={'id': 'email', 'placeholder': 'example@gmail.com'}),
			'mobile_no': forms.NumberInput(attrs={'id': 'mobile_no', 'placeholder': 'Mobile Number'}),
			'name_in_game': forms.TextInput(attrs={'id': 'name_in_game', 'placeholder': 'Game Id Name'}),
			'game_id': forms.NumberInput(attrs={'id': 'game_id', 'placeholder': 'Game Id Number'}),
			'age': forms.NumberInput(attrs={'id': 'age', 'placeholder': 'Age'}),
			'gender': forms.Select(attrs={'id': 'gender'}),
			'facebook_name': forms.TextInput(attrs={'id': 'facebook_name', 'placeholder': 'Facebook Id Name'}),
		}
