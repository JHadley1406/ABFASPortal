from django.db import models
from usermodule.models import PodUser
from jsonfield import JSONField

# Create your models here.
class WhatsUpData(models.Model):
    user_id = models.ForeignKey(PodUser)
    action_id = models.ForeignKey('WhatsUpActions')
    whats_up_text = models.TextField()
    created_on = models.DateTimeField(auto_now_add = True)
    last_updated = models.DateTimeField(auto_now_add = True)

<<<<<<< HEAD
    def __unicode__(self):
        return self.user_id.first_name + ": " + \
               self.action_id.action_text + " " + \
               self.whats_up_text
=======
    json_data = JSONField(default={}, blank=True)


>>>>>>> fa05dd3f832a33b11158f4b31ebc6b903aaa4baa

class WhatsUpActions(models.Model):
    action_text = models.CharField(max_length = 32)
    created_on = models.DateTimeField(auto_now_add = True)

    def __unicode__(self):
        return self.action_text
