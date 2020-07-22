from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import Clubform,Userform,Projectform,Reportform
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .decorators import unauthenticated_user,allowed_users,admin_only
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required

context={}
# Create your views here.
@unauthenticated_user
def adminlogin(request):

    return  render(request,'admintemplates/login.html')

def logoutuser(request):
    logout(request)
    return redirect('login')

#Register clubs
@login_required(login_url='login')
@admin_only
def register_club(request):

    if request.method == 'POST':
        form=Clubform(request.POST)
        print(request.POST)
        dictionary={'csrfmiddlewaretoken':request.POST.get('csrfmiddlewaretoken'),
                    'username':request.POST.get('Username'),
                    'password1':request.POST.get('Password'),
                    'password2':request.POST.get('Password')}
       
        if form.is_valid():
            form.save()
            from django.http import QueryDict
            query_dict = QueryDict('', mutable=True)
            query_dict.update(dictionary)
            userform=UserCreationForm(query_dict)
            print(query_dict)
            try:
                user=userform.save()
                group=Group.objects.get(name='customer')
                user.groups.add(group)
                print('username saved succesfully')
            except:
                print('error')
            user=form.cleaned_data.get('Username')
            messages.success(request,'Registration Successful for '+ str(user))
            return render(request,'admintemplates/club_registration_form.html')
    return render(request,'admintemplates/club_registration_form.html')

# adminhome to display all club list

@login_required(login_url='login')
@admin_only
def clublist(request):
    clubs=Clubs.objects.all()
    return  render(request,'admintemplates/clubs.html',{'clubs':clubs})


def club_home(request):
    if request.method == 'POST':
        username=request.POST.get('Username')
        password=request.POST.get('Password')
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('clublist')
        # logindetails=request.POST.
        # if logindetails['Username']=="rotract@gmail.com" and logindetails['Password']=="super@123":
        #     print('method called suucessfuly')
        #     clubs=Clubs.objects.all()
        #     return  render(request,'admintemplates/clubs.html',{'clubs':clubs})
        # elif user is not None:
        #     login(request,user)
        #     return HttpResponse('user page')

        else:
            messages.info(request,'Username/Password is incorrect')   
            return redirect('login')
            #return render(request,'admintemplates/login.html')

    if request.GET['BackNav']=='Back':
        return redirect('clublist')



#----------------------------------------------------------------------------------------------------
#user screens and redirection API
@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def projecthome(request):
    projects=Projects.objects.filter(Username=request.user,Status='active')
    
    return render(request,'admintemplates/projects.html',{'projects':projects})

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def createproject(request):
    if request.method == 'POST':
        form=Projectform(request.POST)
        print(request.POST)
        current_user=User.objects.get(username=request.user)
        print(current_user)
        if form.is_valid():
            try:
                new_project=form.save(commit=False)
                new_project.Username=current_user
                new_project.save()
                print('saved')
            except:
                print('something went wrong'+str(form.errors))
        else:
            print('notvalid'+str(form.errors))
        ProjectTitle=form.cleaned_data.get('ProjectTitle')
        messages.success(request,'Registration Successful for '+ str(ProjectTitle))
        return render(request,'admintemplates/project_creation.html')
    #projectform=Projectform()
    return render(request,'admintemplates/project_creation.html',{'user':request.user})

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def projectreport(request):
    if request.GET['dropdown_report']=='multiple':
        fProjects=Projects.objects.filter(Username=request.user,Status='active')
        return render(request,'admintemplates/project_add_report.html',{'projects':fProjects})
    else:
        fProjects=Projects.objects.get(Username=request.user,Status='active',pk=request.GET['single_report'])
        print(fProjects)
        return render(request,'admintemplates/project_add_report.html',{'projects':fProjects})

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def addreport(request):
    if request.method == 'POST':
        print(request.POST)
        print('kmfrmv')
        
        form=Reportform(request.POST)
        print(form)
        return HttpResponse('frnefjnr')
        # print(request.POST)
        # pid=Projects.objects.get(ProjectTitle=form.cleaned_data.get('ProjectTitle'))
        # print(pid)
        # if form.is_valid():
        #     try:
        #         new_report=form.save(commit=False)
        #         new_report.ProjectId=pid
        #         new_report.save()
        #         updateproject=Projects.objects.get(pk=pid)
        #         updateproject.Status='inactive'
        #         updateproject.save()
        #         print('saved')
        #         ProjectTitle=form.cleaned_data.get('ProjectTitle')
        #         messages.success(request,'Report generated Successfully for '+ str(ProjectTitle))
        #         return render(request,'admintemplates/project_creation.html')
                
        #     except:
        #         print('something went wrong'+str(form.errors))
        # else:
        #     print('notvalid'+str(form.errors))

#-----------------------------------------------------------------------------------

#Meetings section

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def meetinghome(request):
   #projects=Projects.objects.filter(Username=request.user,Status='active')
    
    return render(request,'admintemplates/meetings.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def createmeeting(request):

    return render(request,'admintemplates/meeting_creation.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def meetingreport(request):


    return render(request,'admintemplates/meeting_add_report.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def meetingaddreport(request):

    return HttpResponse('frnefjnr')



#--------------------------------------------------------------------------------------------


#Membership section


@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def membershiphome(request):
   #projects=Projects.objects.filter(Username=request.user,Status='active')
    
    return render(request,'admintemplates/membership.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def membershipcreation(request):

    return render(request,'admintemplates/member_creation.html')