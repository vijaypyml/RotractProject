from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Clubs(models.Model):

    ClubName =  models.CharField(max_length=200,null=True)
    ClubID   =  models.IntegerField(null=True)
    Group   =   models.CharField(max_length=200,null=True)
    Sponsoring  =   models.CharField(max_length=200,null=True)
    President_Name  =   models.CharField(max_length=200,null=True)
    President_Mail  =   models.EmailField(null=True)
    Secretary_Name  =   models.CharField(max_length=200,null=True)
    Secretary_Mail  =   models.EmailField(null=True)
    Username    =   models.CharField(max_length=200,null=True)
    Password    =   models.CharField(max_length=32,null=True)
    Sponsoring_Mail =   models.EmailField(null=True)
    Group_Mail  =   models.EmailField(null=True)
    District_Mail   =   models.EmailField(null=True)
    Registered_Date =   models.DateTimeField(auto_now_add=True,null=True)


class Projects(models.Model):
    Username    =   models.ForeignKey(User,max_length=32,null=True,on_delete=models.CASCADE)
    ProjectId   =   models.AutoField(primary_key=True)
    ProjectTitle=   models.CharField(max_length=200,null=True)
    ProjectType =   models.CharField(max_length=200,null=True)
    ProjectDate =   models.DateTimeField(null=True)
    PrjectTime  =   models.TimeField(null=True)
    Venue       =   models.CharField(max_length=200,null=True)
    EventChair  =   models.CharField(max_length=200,null=True)
    Speaker     =   models.CharField(max_length=200,null=True)
    Avenue      =   models.CharField(max_length=200,null=True)
    Description =   models.CharField(max_length=200,null=True)
    PoterPic    =   models.ImageField(null=True,blank=True)
    Status      =   models.CharField(max_length=10,default='active')

class Reports(models.Model):
    ProjectId   =   models.ForeignKey(Projects,max_length=32,null=True,on_delete=models.DO_NOTHING)
    ReportId    =   models.AutoField(primary_key=True)
    ProjectTitle=   models.CharField(max_length=200,null=True)
    NoofClubMembers= models.CharField(max_length=200,null=True)
    NoofOtherClubMembers= models.CharField(max_length=200,null=True)
    NoofCouncilMembers= models.CharField(max_length=200,null=True)
    Duration= models.CharField(max_length=200,null=True)
    ProjectDescription= models.CharField(max_length=200,null=True)
    ReportPic    =   models.ImageField(null=True,blank=True)