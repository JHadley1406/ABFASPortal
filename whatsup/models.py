from django.db import models
from usermodule.models import PodUser

# Create your models here.
class WhatsUpData(models.Model):
    user_id = models.ForeignKey(PodUser)
    action_id = models.ForeignKey('WhatsUpActions')
    whats_up_text = models.TextField()
    created_on = models.DateTimeField(auto_now_add = True)
    last_updated = models.DateTimeField(auto_now_add = True)

class WhatsUpActions(models.Model):
    action_text = models.CharField(max_length = 32)
    created_on = models.DateTimeField(auto_now_add = True)