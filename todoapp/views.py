from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import todo

@login_required
def home(request):
    todos = todo.objects.filter(user=request.user)
    return render(request, 'todoapp/index.html', {'todos': todos})

@login_required
def create_task(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        todo.objects.create(user=request.user, todo_name=task, status='Pending')
    return redirect('home-page')

def register(request):
    if request.user.is_authenticated:
        return redirect('home-page')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if len(password) < 3:
            messages.error(request, 'Password must be at least 3 characters')
            return redirect('register-page')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Error, username already exists, use another.')
            return redirect('register-page')

        User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, 'User successfully created, log in now')
        return redirect('login-page')

    return render(request, 'todoapp/register.html')

def login_page(request):
    if request.user.is_authenticated:
        return redirect('home-page')

    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('home-page')
        else:
            messages.error(request, 'Error, wrong user details or user does not exist')
            return redirect('login-page')

    return render(request, 'todoapp/login.html')

def logout_view(request):
    logout(request)
    return redirect('login-page')

@login_required
def delete_task(request, id):
    todo.objects.filter(user=request.user, id=id).delete()
    return redirect('home-page')

@login_required
def update_task(request, id):
    if request.method == 'POST':
        status = request.POST.get('status')
        todo_item = todo.objects.filter(user=request.user, id=id).first()
        if todo_item:
            todo_item.status = status
            todo_item.save()
    return redirect('home-page')
