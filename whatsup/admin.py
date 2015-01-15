from django.contrib import admin
from usermodule.models import PodUser

from whatsup.models import WhatsUpData, WhatsUpActions
# Register your models here.
admin.site.register(WhatsUpData)
admin.site.register(WhatsUpActions)