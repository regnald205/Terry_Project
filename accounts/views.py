from django.shortcuts import render,redirect
from django.contrib import messages,auth
from contacts.models import Contact
from django.contrib.auth.models import User


# Create your views here.
def register(request):
    if request.method == 'POST':
     #get from values
     first_name=request.POST['first_name']
     last_name=request.POST['last_name']
     username=request.POST['username']
     email=request.POST['email']
     password=request.POST['password']
     password2=request.POST['password2']

     #check if passwords match
     if password == password2:
         #check username is not duplicated
           if User.objects.filter(username=username).exists():
              messages.error(request,"that username is taken")
              return redirect('register')

         #check email
           else:
              if User.objects.filter(email=email).exists():
                messages.error(request,"that email is being used")
                return redirect('register')

              else:
                #create user
                user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
           #when you want the user to login after they registered
           #auth.login(request,user)
           #messages.success(request,'You are now logged in')
           #return redirect('index')

           #But i want the user to manually login after they register
                user.save()
                messages.success(request,'you are now registered and can log in')
                return redirect('login')
     else:
           messages.error(request,'password do not match')
           return redirect('register')
      
    else:
        return render(request,'accounts/register.html')

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']

        #to be able to login we create a variable
        user=auth.authenticate(username=username,password=password)
        
        #if user is found
        if user is not None:
            auth.login(request,user)
            messages.success(request,'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request,'invalid credentials')
            return redirect('login')
                 
       
     
    else:
       return render(request,'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,'You are now logout')
        return redirect('index')

    return redirect('index')

def dashboard(request):
    user_contacts=Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)#field we want to filter is user_id

    context={
        'contacts':user_contacts
    }
    return render(request,'accounts/dashboard.html',context) 


