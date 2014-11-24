from django.conf.urls import patterns, include, url
#from usermodule.views import login_user
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pod.views.home',  name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'usermodule.views.index', name="index"),
    url(r'^pod_demo/$', 'usermodule.views.pod_demo', name="pod_demo"),
    url(r'^login/$', 'usermodule.views.login_user', name="login"),
    url(r'^logout/$', 'usermodule.views.logout_user', name="logout"),
    url(r'^board/', 'usermodule.views.meet_the_board', name="board"),
    url(r'^forum/$', 'forum.views.forum_list', name="forums"),
    url(r'^threads/(\d+)$', 'forum.views.thread_list', name="threads"),
    url(r'^thread/(\d+)$', 'forum.views.thread', name="thread"),
    url(r'^add_forum/$', 'forum.views.add_forum', name="addForum"),
    url(r'^add_thread/$', 'forum.views.add_thread', name="addThread"),
    url(r'^add_comment/$', 'forum.views.add_comment', name="addCommentNone"),
    url(r'^add_comment/(\d+)$', 'forum.views.add_comment', name="addComment"),
    url(r'^edit_comment/(\d+)$', 'forum.views.edit_comment', name="editComment"),
    url(r'^whatsup/', 'whatsup.views.whatsup_list', name="whatsup"),
    url(r'^add_whatsup/', 'whatsup.views.add_whatsup', name="addWhatsUp"),
    )
