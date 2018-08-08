from . import forms
from django.db.models import Count
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .models import Service, User, Memo
from .forms import ServiceForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
import PyPDF2

def signup_view(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
		    user = form.save()
		    login(request, user)
			#login user
		return redirect('orders:orders_view')
	else:
		form = UserCreationForm()
	return render(request, 'orders/signup.html', {'form': form})

#/login
def login_view(request):
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request, user)
			if 'next' in request.POST:
				return redirect(request.POST.get('next'))
			else:

				return redirect('orders:home')
	else:
		form = AuthenticationForm()
	return render(request, 'orders/login.html', {'form': form})

#Logout
def logout_view(request):
	if request.method == 'POST':
		logout(request)
		return redirect('orders:login')



#Home
@login_required(login_url='/orders/login/')
def home(request):
	template_name = 'orders/home.html'
	count = Service.objects.count()
	context = { 'count': count,
				'user': request.user }
	return render(request, template_name, context)


#index_list
@login_required(login_url='/orders/login/')
def services(request):
	template_name = 'orders/index.html'
	#service = Service.objects.get(pk=pk)
	service_list = Service.objects.order_by('time')
	context = {'service_list':service_list}
	return render(request, template_name, context)


@login_required(login_url='/orders/login/')
def service_create(request):
	if request.method == 'POST':
		form = forms.ServiceForm(request.POST, request.FILES)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.office = request.user
			instance.save()
			return redirect('orders:dash')	
	else:
		form = forms.ServiceForm()
	return render(request, 'orders/order_create.html', {'form': form})

#Create service
@login_required(login_url='/orders/login/')
class DetailView(generic.DetailView):
	model = User
	template_name = 'orders/detail.html'

#@login_required(login_url='/accounts/login/')
class StatusUpdate(UpdateView):
	model = Service
	fields = ['location', 'service', 'quantity', 'time', 'status_choices', 'cancelled']
	success_url = reverse_lazy('orders:orders_view')

#@login_required(login_url='/accounts/login/')
class ServiceDelete(DeleteView):	
	model = Service
	success_url = reverse_lazy('orders:dash')  

#Toggle 
def complete_service(request, pk):
	service = Service.objects.get(pk=pk)
	service.complete = True
	service.save()
	return redirect('services')

def dashboard(request):
	template_name = 'orders/dashboard.html'
	dashboard = Service.objects.order_by('time')
	context = {'dashboard': dashboard}
	return render(request, template_name, context)







#Pantry todo list
def pantry_todo(request):
	template_name = 'orders/pantry.html'
	pantry = "Pantry List"
	context = {'pantry': pantry}
	return render(request, template_name, context)

def ticket_list(request):
	template_name = 'orders/ticket.html'
	ticket = "Ticket List"
	context = {'ticket': ticket}
	return render(request, template_name, context)

def memo(request):
	template_name = 'orders/memo.html'
	memo_list = Memo.objects.order_by('id')
	context = {'memo_list': memo_list}
	return render(request, template_name, context)

def dashboard(request):
	template_name = 'orders/dashboard.html'
	service_dash = Service.objects.order_by('time')
	context = {'service_dash': service_dash}
	return render(request, template_name, context)

def pdf(request): 
	file = open('my.pdf', 'rb')
	reader = PyPDF2.PdfFileReader(file)
	page = readeer.getPage(0)
	print(page.extractText())

	