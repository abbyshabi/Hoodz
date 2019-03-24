from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm,BusinessForm,ProjectForm,BusinessForm,PostForm
from .models import Business,Profile,Project,Post
from django.contrib.auth.models import User
from django.http import JsonResponse

# Create your views here.
def index(request):
    current_user = request.user
    
    projects = Project.objects.order_by('-date')
    business = Business.objects.all()
    profile = Profile.objects.order_by('-last_update')

    return render(request,'index.html',{"business":business,"profile":profile,"projects":projects})


@login_required(login_url='/accounts/login/')
def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.admin = current_user
            project.save()
        return redirect('home')
    else:
        form = ProjectForm()
    return render(request,'new_project.html',{'form':form})


@login_required(login_url='/accounts/login/')
def profile(request):
    user = request.user
    #profile = Profile.objects.get(user_id=current_user.id)
    
    return render(request, 'profile.html',{"user":user, "current_user":request.user})

@login_required(login_url='/accounts/login/')
def update_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect ('profile')
    else:
        form = ProfileForm()
    
    return render(request,'update_profile.html',{"form":form})

@login_required(login_url='/accounts/login/')
def new_hood(request):
    current_user = request.user
    if request.method == 'POST':
        form = NeighbourhoodForm(request.POST,request.FILES)
        if form.is_valid():
            neighbourhood = form.save(commit=False)
            neighbourhood.hood_admin= current_user
            neighbourhood.save()
        return redirect('home')
    else:
        form = NeighbourhoodForm()
    
    return render(request,'new_hood.html',{"form":form})
