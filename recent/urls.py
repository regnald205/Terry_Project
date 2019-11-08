from . import views
from django.urls import path

urlpatterns=[
    path('',views.index,name="index"),
    path('base/',views.base,name="base"),
    path('about/',views.about,name="about"),
   

]


 #path('project/',views.project,name="project")