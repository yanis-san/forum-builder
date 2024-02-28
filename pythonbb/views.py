from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.urls import reverse
from pythonbb.models import Forum, Thread, Message
from authentication.models import UserForum,User
from pythonbb.forms import CreateForumForm, CreateMessageForm, CreateThreadForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group



def index(request):
    forums = Forum.objects.order_by("-created_at").all()
    admin_groupe = Group.objects.get(name='Administrateur')
    is_admin = UserForum.objects.filter(user=request.user, groupe = admin_groupe).exists()
    context = {"forums": forums, 'is_admin': is_admin}
    return render(request, "pythonbb/index.html",context)




@login_required
def forum(request, forum_slug):
    user = request.user
    forum = Forum.objects.get(slug=forum_slug)
    is_member = UserForum.objects.filter(user=user,forum=forum).exists()
    if not is_member:
        return render(request,'pythonbb/join_forum.html', context={"forum": forum})
    
    threads = Thread.objects.filter(forum=forum)
    context = {"forum": forum, "threads":threads}

    return render(request, "pythonbb/forum_index.html",context)


@login_required
def join_forum(request,forum_slug):
    user = request.user
    forum = Forum.objects.get(slug=forum_slug)
    member_groupe = Group.objects.get(name='Membre')
    UserForum.objects.create(user=user, forum=forum, groupe=member_groupe)

    return redirect('pythonbb:forum',forum_slug=forum_slug)




@login_required
def create_forum(request):
    if request.method == "POST":
        form=CreateForumForm(request.POST)
        if form.is_valid():
            forum = form.save()
            admin_groupe = Group.objects.get(name='Administrateur')
            UserForum.objects.create(user=request.user,forum=forum, groupe=admin_groupe)
            return redirect("pythonbb:index")
    else:
        form = CreateForumForm()

    return render(request,"pythonbb/create_forum.html", context={'form':form})




@login_required
def forum_update(request,forum_slug):
    forum = Forum.objects.get(slug=forum_slug)
    form = CreateForumForm(instance=forum)
    admin_groupe = Group.objects.get(name='Administrateur')
    is_admin = UserForum.objects.filter(user=request.user,forum=forum, groupe = admin_groupe).exists()

    if is_admin:
        if request.method == "POST":
            form = CreateForumForm(request.POST,instance=forum)

            if form.is_valid():
                form.save()
                return redirect("pythonbb:index")
    else :
        return HttpResponse("<h1> Vous n'avez pas le droit de modifier ce forum</h1")
        
    return render(request,"pythonbb/update_forum.html",{"forum":forum,"form": form})




@login_required
def forum_delete(request,forum_slug):
    forum = Forum.objects.get(slug=forum_slug)
    admin_groupe = Group.objects.get(name='Administrateur')
    is_admin = UserForum.objects.filter(user=request.user,forum=forum, groupe = admin_groupe).exists()
    if is_admin:
        if request.method == "POST":
            forum.delete()
            return redirect("pythonbb:index")
    else : 
        return HttpResponse("<h1> Vous n'avez pas le droit de supprimer ce forum</h1")
    
    return render(request,"pythonbb/delete_forum.html",{"forum":forum})





@login_required
def thread_index(request, forum_slug, thread_slug):
    forum = Forum.objects.get(slug=forum_slug)
    thread = Thread.objects.get(slug=thread_slug)
    messages = thread.message_set.all()

    form = CreateMessageForm()
    member_group = Group.objects.get(name='Membre')
    is_member = UserForum.objects.filter(user=request.user, forum=forum, groupe=member_group).exists()
    admin_group = Group.objects.get(name='Administrateur')
    is_admin = UserForum.objects.filter(user=request.user, forum=forum, groupe=admin_group).exists()
    modo_groupe = Group.objects.get(name='Modérateur')
    is_modo = UserForum.objects.filter(user=request.user,forum=forum, groupe = modo_groupe).exists()
    
    if is_member or is_admin:
        if request.method == "POST":
            form = CreateMessageForm(request.POST)
            if form.is_valid():
                message = form.save(commit=False)
                message.thread = thread
                message.save()
                return redirect("pythonbb:thread-index", forum_slug=forum_slug, thread_slug=thread_slug)

        context = {
            "thread": thread,  
            "messages": messages,
            "form": form,
            "forum_slug": forum_slug,  
            "thread_slug": thread_slug,
            "is_admin": is_admin,
            "is_modo" : is_modo, 
        }
        return render(request, "pythonbb/thread_index.html", context)
    return HttpResponse("<h1>Vous n'avez pas le droit</h1>")




@login_required
def create_thread(request, forum_slug):
    forum = Forum.objects.get(slug=forum_slug)

    form = CreateThreadForm()
    member_groupe = Group.objects.get(name='Membre')
    admin_groupe = Group.objects.get(name='Administrateur')
    is_member = UserForum.objects.filter(user=request.user,forum=forum, groupe = member_groupe).exists()
    is_admin = UserForum.objects.filter(user=request.user,forum=forum, groupe = admin_groupe).exists()

    if is_member or is_admin :
        if request.method == "POST":
            form=CreateThreadForm(request.POST)
            if form.is_valid():
                thread = form.save(commit=False)
                thread.forum = forum
                thread.save()
                return redirect("pythonbb:forum", forum_slug=forum.slug)
        else:
            form = CreateThreadForm()
        return render(request,"pythonbb/create_thread.html", context={'forum':forum,'form':form})
    
    return HttpResponse("<h1>Vous n'avez pas le droit</h1>")


@login_required
def thread_delete(request,forum_slug,thread_slug):
    forum = Forum.objects.get(slug=forum_slug)
    thread = Thread.objects.get(slug=thread_slug)
    admin_groupe = Group.objects.get(name='Administrateur')
    is_admin = UserForum.objects.filter(user=request.user,forum=forum, groupe = admin_groupe).exists()
    modo_groupe = Group.objects.get(name='Modérateur')
    is_modo = UserForum.objects.filter(user=request.user,forum=forum, groupe = modo_groupe).exists()
    
    if is_admin or is_modo :
        if request.method == "POST":
            thread.delete()
            return redirect("pythonbb:forum" , forum_slug=forum_slug) 
            
        return render(request,"pythonbb/delete_thread.html",{"thread":thread, "forum":forum})
    
    return HttpResponse("<h1>Vous n'avez pas le droit</h1>")



@login_required
def message_ban(request, forum_slug, thread_slug, message_id):
    forum = Forum.objects.get(slug=forum_slug)
    thread = Thread.objects.get(slug=thread_slug)
    admin_groupe = Group.objects.get(name='Administrateur')
    modo_groupe = Group.objects.get(name='Modérateur')
    is_admin = UserForum.objects.filter(user=request.user,forum=forum, groupe = admin_groupe).exists()
    is_modo = UserForum.objects.filter(user=request.user,forum=forum, groupe = modo_groupe).exists()
    
    if is_admin or is_modo:
        if request.method == "POST":
            message = get_object_or_404(Message, id=message_id)
            message.ban = True
            message.save()
            return redirect("pythonbb:thread-index", forum_slug=forum_slug, thread_slug=thread_slug)
    
    return HttpResponse("<h1>Vous devez être modérateur ou administrateur</h1>")


 