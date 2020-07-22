from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.adminlogin,name='login'),
    path('logout/', views.logoutuser,name='logout'),
    #admin redirection urls
    path('clubregister/',views.register_club,name='clubregister'),
    path('adminhome/',views.club_home,name='adminhome'),
    path('home/',views.clublist,name='clublist'),

    #User Redirection URLs

    #project URLs
    path('projects/',views.projecthome,name='projecthome'),
    path('create_projects/',views.createproject,name='createproject'),
    path('create_project_report/',views.projectreport,name='projectreport'),
    path('reportadded/',views.addreport,name='addreport'),

    #meeting URLs
    path('meetings/',views.meetinghome,name='meetinghome'),
    path('create_meeting/',views.createmeeting,name='createmeeting'),
    path('create_meeting_report/',views.meetingreport,name='meetingreport'),
    path('reporadded/',views.meetingaddreport,name='meetingaddreport'),

    #membership URLs

    path('members_home/',views.membershiphome,name='membershiphome'),
    path('create_members/',views.membershipcreation,name='membershipcreation')


]
