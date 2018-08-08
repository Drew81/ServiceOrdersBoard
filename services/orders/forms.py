from django import forms

from .models import Service




class ServiceForm(forms.ModelForm):

	class Meta:
		model = Service
		fields = ['location', 'service', 'quantity', 'time', 'status_choices', 'cancelled']

class StatusUpdate(forms.ModelForm):

	class Meta:
		model = Service
		fields = ['location', 'service', 'quantity', 'time', 'status_choices', 'cancelled']


class ServiceDelete(forms.Form):
	class Meta:
		model = Service
		fields = ['__all__']