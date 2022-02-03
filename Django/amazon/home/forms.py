from django import forms
from .models import MyTracks , MyRegister2
class addstudent(forms.Form):
    userName = forms.CharField(label='user name' , max_length=30)
    password2 = forms.CharField( label='password',max_length=30)
    email = forms.EmailField(label='E-Mail' , max_length=30)
    track_id = forms.ChoiceField(choices=[(track.id ,track.mytrack) for track in MyTracks.objects.all()])


class addstudentFormGUI(forms.ModelForm):
    class Meta:
        fields='__all__'
        model=MyRegister2
