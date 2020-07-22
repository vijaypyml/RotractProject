from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Clubs,Projects,Reports

class Reportform(ModelForm):
    class meta:
        model=Reports
        fields = '__all__'
        
class Clubform(ModelForm):
    class Meta:
        model=Clubs
        fields = '__all__'


class Userform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1','password2']

class Projectform(ModelForm):
    class Meta:
        model=Projects
        exclude=('Username','Status')

