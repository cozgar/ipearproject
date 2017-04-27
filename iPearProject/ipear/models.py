from django.db import models
from django import forms
# Create your models here.

'''
class CreateUser(models.Model):
	username = models.CharField(max_length=220)	

	def __str__(self):
		return str(self.username)


class UserForm(forms.ModelForm):
	class Meta:
		exclude = ('user',)

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		exclude = ['user']

'''
'''
python manage.py makemigrations
python manage.py migrate

'''
