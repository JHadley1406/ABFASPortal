from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from models import Thread, Post, Forum
from django.template import RequestContext


# output views
def forum_list(request):
    request.session['call_page'] = "forums"
    request.session['args_val'] = []
    return render_to_response("forum/forum_list.html",
                              dict(forums=Forum.objects.all()), RequestContext(request))


def thread_list(request, forum_number):  # added last_posts list for last post display support
    last_posts = []
    request.session['forum_number'] = request.session['args_val'] = forum_number
    request.session['call_page'] = "threads"
    threads = Thread.objects.filter(forum=request.session.get('forum_number'))
    for individualThread in threads:
		if Post.objects.filter(thread=individualThread):
			last_posts.append(Post.objects.filter(thread=individualThread).latest('created_on'))
    return render_to_response("forum/thread_list.html",
                              dict(threads=threads,
                                   last_posts=last_posts,
                                   parent_forum=Forum.objects.get(pk=request.session.get('forum_number'))),
                              RequestContext(request))


def thread(request, thread_number):
    request.session['thread_number'] = request.session['args_val'] = thread_number
    request.session['call_page'] = "thread"
    return render_to_response("forum/thread.html",
                              dict(posts=get_comments(Post.objects
                                                      .filter(thread=thread_number,parent_post__isnull=True)
                                                      .order_by('votes', 'created_on')),
                                   parent_thread=Thread.objects.get(pk=request.session.get('thread_number')),
                                   parent_forum=Forum.objects.get(pk=request.session.get('forum_number'))),
                              RequestContext(request))


# input views
def add_forum(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse(request.session['call_page']))
    if request.POST:
        insert_forum(request)
        return render_to_response("forum/forum_list.html",
                                  dict(forums=Forum.objects.all()),
                                  RequestContext(request))
    else:
        return render_to_response("forum/add_forum.html",
                                  RequestContext(request))


def add_thread(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse(request.session['call_page'], args=(request.session['args_val'])))
    forum_number = request.session.get('forum_number')
    if request.POST:
        insert_thread(request)
        return render_to_response("forum/thread_list.html",
                                  dict(threads=Thread.objects.filter(forum=forum_number),
                                       forum_number=forum_number,
                                       parent_forum=Forum.objects.get(pk=request.session.get('forum_number'))),
                                  RequestContext(request))
    else:
        return render_to_response("forum/add_thread.html",
                                  dict(forum_number=forum_number),
                                  RequestContext(request))


def add_comment(request, parent_comment):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse(request.session['call_page'], args=(request.session['args_val'])))
    thread_number = request.session.get('thread_number')
    if request.POST:
        insert_comment(request, parent_comment)
        return render_to_response("forum/thread.html",
                                  dict(posts=get_comments(Post.objects
                                                          .filter(thread=thread_number,parent_post__isnull=True)
                                                          .order_by('votes', 'created_on')),
                                       thread_number=thread_number,
                                       parent_thread=Thread.objects.get(pk=thread_number),
                                       parent_forum=Forum.objects.get(pk=request.session.get('forum_number'))),
                                  RequestContext(request))
    else:
        return render_to_response("forum/add_post.html",
                                  dict(thread_number=thread_number,
                                       parent_comment=parent_comment),
                                  RequestContext(request))


def edit_comment(request, comment_id):
    comment = Post.objects.get(pk=comment_id)
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse(request.session['call_page'], args=(request.session['args_val'])))
    if request.POST:
        comment.text = request.POST.get('text')
        comment.save(update_fields=['text'])
        return render_to_response("forum/thread.html",
                                  dict(posts=get_comments(Post.objects
                                                          .filter(parent_post__isnull=True)
                                                          .order_by('votes', 'created_on')),
                                       thread_number=request.session.get('thread_number'),
                                       parent_thread=Thread.objects.get(pk=request.session.get('thread_number')),
                                       parent_forum=Forum.objects.get(pk=request.session.get('forum_number'))),
                                  RequestContext(request))
    else:
        return render_to_response("forum/edit_post.html",
                                  dict(comment=comment),
                                  RequestContext(request))


def get_comments(tier_one):
    comment_list = []
    for post in tier_one:
        comment_list.extend(get_n_tier(post))
    return comment_list


def get_n_tier(parent_post):
    comment_list = [parent_post]
    posts = Post.objects.filter(parent_post=parent_post.id)
    if posts:
        for post in posts:
            comment_list.extend(get_n_tier(post))
    return comment_list


def insert_comment(request, parent_comment):
    if parent_comment == '0':
        parent_comment_obj = None
        tier = 0
    else:
        parent_comment_obj = Post.objects.get(pk=parent_comment)
        if parent_comment_obj.tier < 4:  # MAX INDENT IS HERE
            tier = parent_comment_obj.tier + 1
        else:
            tier = parent_comment_obj.tier
    post = Post.objects.create(text=request.POST.get('text'),
                               created_by=request.user,
                               thread=Thread.objects.get(pk=request.session.get('thread_number')),
                               parent_post=parent_comment_obj,
                               tier=tier)
    post.save()


def insert_thread(request):
    new_thread = Thread.objects.create(title=request.POST.get('title'),
                                       created_by=request.user,
                                       forum=Forum.objects.get(pk=request.session.get('forum_number')))
    new_thread.save()


def insert_forum(request):
    forum = Forum.objects.create(title=request.POST.get('title'),
                                 description=request.POST.get('description'),
                                 created_by=request.user)
    forum.save()