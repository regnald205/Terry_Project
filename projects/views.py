from django.shortcuts import render,get_object_or_404
from .models import Projects
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from  .choices import prices_choices,bedroom_choices



# Create your views here.
def index(request):
    #if you want to order it by date
    #FILTER function is used to specify which data may be displayed
    projects=Projects.objects.order_by('list_date').filter(is_published=True)

    paginator=Paginator(projects,6)#Paginator function it carry two values one is from models define and other is page number
    
    page=request.GET.get('page')
    paged_projects=paginator.get_page(page)
    
    context={
        'projects': paged_projects
    }
    return render(request,'projects/projects.html',context)

def search(request):
    queryset_list=Projects.objects.order_by('-list_date')

    #for keywords search
    if 'keywords' in request.GET:
     keywords=request.GET['keywords']
    #make sure keywords is not an empty string
     if keywords:
        queryset_list=queryset_list.filter(description__icontains=keywords)

    #search for city
    if 'city' in request.GET:
        city=request.GET['city']
        if city:
            queryset_list=queryset_list.filter(city__iexact=city)#"i" for case sensitive 

    
    #search for bedrooms
    if 'bedrooms' in request.GET:
        bedrooms=request.GET['bedrooms']  
        if bedrooms:
            queryset_list=queryset_list.filter(bedrooms__lte=bedrooms) 

      #search for price
    if 'price' in request.GET:
        price=request.GET['price']  
        if price:
            queryset_list=queryset_list.filter(price__iexact=price)#"i" for case sensitive           
                  

    context={
       'bedroom_choices': bedroom_choices,
      
       'prices_choices': prices_choices,
       'projects': queryset_list,
       'values': request.GET
    
    }
    return render(request,'projects/search.html',context)   

def project(request,project_id):
    project = get_object_or_404(Projects,pk=project_id)
    context = {
        'project':project
    }
    return render(request,'projects/project.html',context)   

