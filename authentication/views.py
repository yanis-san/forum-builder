from django.shortcuts import render, redirect
from authentication.forms import LoginForm, SignupForumForm
from django.contrib.auth import login, authenticate,logout

def login_page(request):
    form = LoginForm()
    message = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username = form.cleaned_data['username'],
                                password = form.cleaned_data['password']
            )
        
            if user is not None:
                login(request,user)
                message = f'Bonjour, {user.username}! Vous êtes connecté.'
                return redirect('pythonbb:index')
            else :
                message = 'Identifiants invalides'

    return render(request, 'authentication/login.html', context={'form':form, 'message':message})


def logout_user(request):
    logout(request)
    return redirect('authentication:login')


def signup_forum(request):
    form = SignupForumForm()
    if request.method == 'POST':
        form = SignupForumForm(request.POST)
        if form.is_valid():
            user = form.save()
            #Connexion auto
            login(request,user)
            return redirect('pythonbb:index')
    return render(request,'authentication/signup_forum.html', context={"form":form})