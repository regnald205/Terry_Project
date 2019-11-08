from django.shortcuts import render
from projects.models import Projects #we access any models even in another apps
from realtor.models import Realtor
from projects.choices import prices_choices,bedroom_choices

def index(request):
  projects=Projects.objects.order_by('-list_date').filter(is_published=True)[:3]
 



  context={
    'projects':projects,  
    'bedroom_choices':bedroom_choices,
    'prices_choices':prices_choices
   
  }
  return render(request,'recent/index.html',context)

def base(request):
  return render(request,'recent/base.html') 

def about(request):
  #Get all realtor
  realtors=Realtor.objects.order_by('hire_date')

  #Get mvp
  mvp_realtors=Realtor.objects.all().filter(is_mvp=True) 

  context={
    'realtors':realtors,
    'mvp_realtors':mvp_realtors
  }


  return render(request,'recent/about.html',context)  

#def project(request):
#   return render(request,'recent/project.html')  







