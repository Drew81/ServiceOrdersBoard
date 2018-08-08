from django.urls import path, re_path
from . import views
from orders.views import service_create, StatusUpdate, ServiceDelete

app_name = 'orders'

urlpatterns = [
    path('', views.services, name='orders_view'),
    path('login/', views.login_view, name='login'),
	path('home/', views.home, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    #path('profile/', views.user_profile, name='profile'),
    #path('detail/<int:pk>/', views.service_detail, name='status_create'),
    path('create/', views.service_create, name='create'),
    re_path(r'^(?P<pk>\d+)/$', StatusUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', ServiceDelete.as_view(), name='delete'),
    path('complete/<int:pk>/', views.complete_service, name='complete'),
    #path('pantry/', views.pantry_todo, name='pantry'),
    #path('tickets/', views.ticket_list, name='tickets'),
    path('dashboard/', views.dashboard, name='dash'),
    #path('memo/', views.memo, name='memos') 
]