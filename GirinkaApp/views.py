# from django.shortcuts import render

from django.shortcuts import  render, redirect
from django.contrib import messages 
from django.views.generic import DetailView, ListView,CreateView,TemplateView
from .models import Announcements
from django.core.files.storage import FileSystemStorage
from .forms import AnnounceForm
from django.urls import reverse
# Create your views here.
class HomeView(TemplateView):
    context = {}

    model=Announcements
    template_name='GirinkaApp/index.html'

def announce_list(request):
    if request.method == 'POST':
       form = AnnounceForm(request.POST, request.FILES)
       if form.is_valid:
        form.save()
        return render(request,'GirinkaApp/announcement.html')
        
    else:
        form = AnnounceForm()

    return render(request,'GirinkaApp/uploadlist.html', { 'form': form })

def AdAnnouncement(request):
    announcement=Announcements.objects.all()

    return render(request,'GirinkaApp/announcement.html', {'announcement': announcement})
    
    
# login link
def login1(request):
    return render(request, 'login1.html')

#imported views
def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("main:homepage")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request=request, template_name="register.html", context={"register_form":form})
    #login form

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("main:homepage")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form":form})