
from django.contrib import admin
from django.urls import include, path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views


urlpatterns = [
    
    #path('home/', views.home),
    #path('accounts/', include('accounts.urls')),
    path('orders/', include('orders.urls')),
    path('admin/', admin.site.urls)

]

urlpatterns += staticfiles_urlpatterns()
#+ static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)