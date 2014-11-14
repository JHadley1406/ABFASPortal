from django.contrib import admin
from models import Forum, Thread, Post, DeletionReason

# Register your models here.
class ForumAdmin(admin.ModelAdmin):
    list_display = ["title", "created_by", "created_on"]

class ThreadAdmin(admin.ModelAdmin):
    list_display = ["title", "votes", "created_by", "created_on"]

class PostAdmin(admin.ModelAdmin):
    list_display = ["votes", "created_by", "created_on"]

class DeletionReasonAdmin(admin.ModelAdmin):
    list_display = ["text", "created_by", "created_on"]


admin.site.register(Forum, ForumAdmin)
admin.site.register(Thread, ThreadAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(DeletionReason, DeletionReasonAdmin)