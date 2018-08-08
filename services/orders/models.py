from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.
from django.utils import timezone




class Service(models.Model):

	STATUS_CHOICES = (
		('Ready', 'READY'),
		('Stand-by', 'STANDBY'),
		('Enroute', 'ENROUTE'),
		('Delivered', 'DELIVERED')
	)

	SERVICE_CHOICES = (
		('AM Break', 'AM_BREAK'),
		('Breakfast', 'BREAKFAST'),
		('Lunch', 'LUNCH'),
		('PM Break', 'PM_BREAK'),
		('Dinner', 'DINNER'),
		('Popup', 'POPUP')
	)

	TIME_CHOICES = (
		('12:00 am', '12:00 am'),
		('12:30 am', '12:30 am'),
		('1:00 am', '1:00 am'),
		('1:30 am', '1:30 am'),
		('2:00 am', '2:00 am'),
		('2:30 am', '2:30 am'),
		('3:00 am', '3:00 am'),
		('4:00 am', '4:00 am'),
		('4:30 am', '4:30 am'),
		('5:00 am', '5:00 am'),
		('5:30 am', '5:30 am'),
		('6:00 am', '6:00 am'),
		('6:30 am', '6:30 am'),
		('7:00 am', '7:00 am'),
		('7:30 am', '7:30 am'),
		('8:00 am', '8:00 am'),
		('8:30 am', '8:30 am'),
		('9:00 am', '9:00 am'),
		('9:30 am', '9:30 am'),
		('10:00 am', '10:00 am'),
		('10:30 am', '10:30 am'),
		('11:00 am', '11:00 am'),
		('11:30 am', '11:30 am'),
		('12:00 pm', '12:00 pm'),
		('12:30 pm', '12:30 pm'),
		('1:00 pm', '1:00 pm'),
		('1:30 pm', '1:30 pm'),
		('2:00 pm', '2:00 pm'),
		('2:30 pm', '2:30 pm'),
		('3:00 pm', '3:00 pm'),
		('4:00 pm', '4:00 pm'),
		('4:30 pm', '4:30 pm'),
		('5:00 pm', '5:00 pm'),
		('5:30 pm', '5:30 pm'),
		('6:00 pm', '6:00 pm'),
		('6:30 pm', '6:30 pm'),
		('7:00 pm', '7:00 pm'),
		('7:30 pm', '7:30 pm'),
		('8:00 pm', '8:00 pm'),
		('8:30 pm', '8:30 pm'),
		('9:00 pm', '9:00 pm'),
		('9:30 pm', '9:30 pm'),
		('10:00 pm', '10:00 pm'),
		('10:30 pm', '10:30 pm'),
		('11:00 pm', '11:00 pm'),
		('11:30 pm', '11:30 pm'),
	)
	location = models.CharField(max_length=200)
	service = models.CharField(max_length=20, choices=SERVICE_CHOICES, default='AM Break')
	quantity = models.CharField(max_length=200)
	time = models.CharField(max_length=200, choices=TIME_CHOICES, default='10:30 am')
	status_choices = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Stand-by')
	added = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(default=timezone.now())
	office = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
	cancelled = models.BooleanField(default=False)
	#file = models.FileField()

	def get_absolute_url(self):
		return reverse('orders:dash')

	def __str__(self):
		return self.location + ' _ ' + self.service + ' _ ' + self.status_choices



class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	company = models.CharField(max_length=200)

	def __str__(self):
		return self.company

def create_profile(sender, **kwargs):
	if kwargs['created']:
		user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)





#class PanrtyService(models.Model):

#	user = models.OneToOneField(User, on_delete=models.CASCADE)
	
class Memo(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	Message = models.CharField(max_length=1000)
	updated = models.DateTimeField(default=timezone.now())

	def __str__(self):
		return self.title

class Events(models.Model):
	ROOM_CHOICES = (
		('115', '115'),
		('118', '118'),
		('121', '121')
		)
	title = models.CharField(max_length=200)
	room = models.CharField(max_length=1, choices=ROOM_CHOICES, default='115')


















	