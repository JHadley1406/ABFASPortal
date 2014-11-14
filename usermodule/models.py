from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PodUser(models.Model):
	user = models.OneToOneField(User)
	is_board_member = models.BooleanField(default=0)
	

class BoardMember(models.Model):
	user_id = models.ForeignKey(User)
	biography = models.TextField()
	member_since = models.IntegerField()
	member_until = models.IntegerField()
	advice = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True)
	
	def __unicode(self):
		return self.biography
	
class BoardPositions(models.Model):
	user_id = models.ForeignKey(User)
	position_text = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True)
	
class Education(models.Model):
	user_id = models.ForeignKey(User)
	education_type = models.ForeignKey('EducationType')
	education_desc = models.TextField()
	education_start = models.DateTimeField()
	education_end = models.DateTimeField()
	created_on = models.DateTimeField(auto_now_add=True)
	
class EducationType(models.Model):
	education_type = models.CharField(max_length=64)
	created_on = models.DateTimeField(auto_now_add=True)
	