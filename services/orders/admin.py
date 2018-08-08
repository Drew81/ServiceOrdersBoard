from django.contrib import admin
from .models import Service, UserProfile, Memo
# Register your models here.


admin.site.register(Service)
admin.site.register(UserProfile)
admin.site.register(Memo)