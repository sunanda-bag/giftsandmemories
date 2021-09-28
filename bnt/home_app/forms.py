from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import *

class SignupForm(UserCreationForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		# self.fields['password1'].label = 'password'
		# self.fields['password2'].label = 'Confirm password'

		self.fields['password1'].help_text = ''
		self.fields['password2'].help_text = ''
		self.fields['username'].help_text = ''


		for field_name, field in self.fields.items():
			self.fields[field_name].widget.attrs['placeholder'] = self.fields[field_name].label
			self.fields[field_name].label = ""
		#message = forms.TextField(label='Message', widget=forms.TextInput(attrs={'placeholder': 'Message'}))
		self.fields['email'].widget.attrs['placeholder'] = 'Email'
	email = forms.EmailField()

	class Meta:
		model=User
		fields=('username','first_name', 'last_name','email','password1','password2')

