from django.shortcuts import render_to_response
from django.template import RequestContext
from models import WhatsUpData, WhatsUpActions
from django.http import HttpResponseRedirect

# Create your views here.
#what'sup main page
def whatsup_list(request):

    return render_to_response("whatsup/whatsup_list.html",
                              dict(whatsUpData=WhatsUpData.objects.all()),
                              RequestContext(request))

#view individual what's up
def whatsup(request, whatsup_number):
    return render_to_response("whatsup/whatsup.html",
                              RequestContext(request))

#add new what's up
def add_whatsup(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect()
    if request.POST:
        #build a whatsup object and post it to the database
    return render_to_response("whatsup/add_whatsup.html",
                              dict(whatsUpActions = WhatsUpActions.objects.all()),
                              RequestContext(request))


