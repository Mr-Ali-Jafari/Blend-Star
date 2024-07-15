from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *
from Index import models as index_model
from django.contrib.auth import authenticate, login, logout
# Create your views here.

@login_required
def profile_detail(request,pk):
    profile = Profile.objects.filter(user=request.user,pk=pk)
    posts = index_model.Post.objects.filter(user=request.user.profile).order_by('-date')
    liked_posts = []

    if request.user.is_authenticated:
            liked_posts = request.user.profile.like_set.values_list('post_id', flat=True)

    return render(request,'account/profile_detail.html',{
        "md":posts,
        "profile":profile,
        "liked_posts":liked_posts,
    })

@login_required
def create_or_edit_profile(request):
    try:
        profile = Profile.objects.get(user=request.user)
        is_edit = True
    except Profile.DoesNotExist:
        profile = None
        is_edit = False

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            new_profile = form.save(commit=False)
            new_profile.user = request.user
            new_profile.save()
            # messages.success(request,'با موفقیت پروفایل ساخته/ادیت شد رفیق','success')
            print("create or edit is successfully :D")
            return redirect('index')
    else:
        form = ProfileForm(instance=profile)

    context = {
        'form': form,
        'is_edit': is_edit,
    }
    
    return render(request, 'account/create_edit_profile.html', context)











def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)

                    return redirect('c_e_profile') 
        else:
            form = AuthenticationForm()
        return render(request, 'account/login.html', {'form': form})
    else:
        return redirect('index')




def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('index')  
    else:
        return redirect('index')



def register_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('c_e_profile')  
        else:
            form = UserCreationForm()
        return render(request, 'account/register.html', {'form': form})
    else:
        return redirect('index')