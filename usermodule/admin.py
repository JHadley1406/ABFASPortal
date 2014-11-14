from django.contrib import admin
from usermodule.models import PodUser, BoardMember, BoardPositions, Education, EducationType
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class PodUserInline(admin.StackedInline):
	model = PodUser
	can_delete = False
	verbose_name_plural = 'podUser'
	
class UserAdmin(UserAdmin):
	inlines = (PodUserInline, )

# Register your models here.
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(BoardMember)
admin.site.register(BoardPositions)
admin.site.register(Education)
admin.site.register(EducationType)