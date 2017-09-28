from django.contrib import admin
from jobapp.models import DynamicGroup , SaltGroup , ExecUser
# Register your models here.



admin.site.register(DynamicGroup)
admin.site.register(SaltGroup)
admin.site.register(ExecUser)

