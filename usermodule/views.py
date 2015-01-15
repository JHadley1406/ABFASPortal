from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from models import Education, EducationType
from django.template import RequestContext
from django.shortcuts import render_to_response


def login_user(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
    return HttpResponseRedirect(reverse(request.session['call_page'], args=(request.session['args_val'])))


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('forums'))


def edit_user(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse(request.session['call_page']))
    podUser = request.session['user'].id
    educationTypes = EducationType.Objects.get()
    education = Education.objects.get(user_id=podUser.id)
    if request.POST:
        podUser.first_name = request.POST.get('first_name')
        podUser.last_name = request.POST.get('last_name')
        podUser.email = request.POST.get('email')
        podUser.save(update_fields=['first_name', 'last_name', 'email'])
        return HttpResponseRedirect(reverse(request.session['call_page']), args=(request.session['args_val']))
    else:
        return HttpResponseRedirect("usermodule/edit_user.html",
                                    dict(user=podUser,
                                         education=education,
                                         educationTypes=educationTypes),
                                    args=[request.session['args_val']])

def index(request):
    return render_to_response("usermodule/index.html",  context_instance=RequestContext(request))

def pod_demo(request):
    return render_to_response("usermodule/pod_demo.html")

def meet_the_board(request):
    return render_to_response("usermodule/meet_the_board.html")