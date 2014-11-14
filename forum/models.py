from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class DeletionReason(models.Model):
    text = models.TextField(max_length=25)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User)

    def __unicode__(self):
        return self.text

class Forum(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField(max_length=256)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User)
    is_locked = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title

class Thread(models.Model):
    title = models.CharField(max_length=60)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User)
    forum = models.ForeignKey(Forum)
    votes = models.IntegerField(default=0)
    is_locked = models.BooleanField(default=False)

    def __unicode__(self):
        return unicode(self.created_by) + " - " + self.title

class Post(models.Model):
    text = models.TextField(max_length=10000)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User)
    thread = models.ForeignKey(Thread)
    parent_post = models.ForeignKey('self', null=True)
    tier = models.IntegerField(default=0)
    is_deleted = models.ForeignKey(DeletionReason, null=True)
    votes = models.IntegerField(default=0)

    def __unicode__(self):
        return u"%s - %s - %s" % (self.created_by, self.thread, self.text)


