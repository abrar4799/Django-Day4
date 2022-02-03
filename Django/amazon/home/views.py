from django.shortcuts import render
from .models import MyRegister2 , MyTracks
from django.shortcuts import redirect , HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import addstudent, addstudentFormGUI
from django.views import View
from django.views.decorators.http import require_http_methods
from django.views.generic import ListView , CreateView

# Create your views here
from django.http import HttpResponse
class studenteCreateView(CreateView):
    model = MyRegister2
    fields = '__all__'
class studentlist(ListView):
    model = MyRegister2

class insertstudentFormModel(View):
    def get(self, request):
        context = {}
        form =addstudentFormGUI()
        context['GUI']=form
        return render(request ,'formModelReg.html',context)
    def post(self , request):
        context={}
        afterform= addstudentFormGUI(request.POST)
        afterform.save()
        return render(request ,'login.html', context)



def index(request,name):
   return HttpResponse(f'<h1>Welcome {name}</h1>')

def navbar(request):
   return render(request , 'nv.html')

def contactus(request):
   return render(request, 'contactus.html')

def about(request):
   return render(request, 'about.html')
@require_http_methods(['GET' , 'POST'])
def studentaddView(request):
    context = {}
    form = addstudent()
    if(request.method == 'GET'):
        context['form']=form
        return render(request,'formRegister.html',context)
    else:
        form=addstudent(request.POST)
        if (form.is_valid()):
           regist = MyTracks.objects.get(id=request.POST['track_id'])
           MyRegister2.objects.create(userName=request.POST['userName'], password2=request.POST['password2'],
                                   email=request.POST['email'] ,track_id_id=regist)

           return render(request , 'login.html' )

       # return redirect(login)
def tracksView(request):
    if (request.method == 'GET'):
        return render(request, 'tracks.html')
    else:
        MyTracks.objects.create(mytrack=request.POST['tracks'])
        return render(login)

def register(request):

   if(request.method == 'GET'):
     return render(request, 'register.html')
   else:
      tractobj = MyTracks.objects.get(mytrack=request.POST['track'])
      MyRegister2.objects.create(userName=request.POST['userName'] , password2=request.POST['password2'] , email=request.POST['email'] , track_id_id=tractobj)
      #User.objects.create_user(username=request.POST['userName'] , password=request.POST['password2'] ,email=request.POST['email'])
      return redirect(login)
def selectedusers(request):
    students =MyRegister2.objects.all()
    context={}
    context['student'] = students
    return render(request , 'student.html' , context)
def delete(request , id):
    MyRegister2.objects.filter(id=id).delete()
    students = MyRegister2.objects.all()
    context ={}
    context['student'] = students
    return render(request, 'student.html', context)
def search(request ):
    if request.method == 'GET':
        userName= request.GET.get('userName')
        students = MyRegister2.objects.filter(userName=userName)
        context = {}
        context['student'] = students
        return render(request, 'search.html', context)

def login(request):
   if(request.method == 'GET'):
      return render(request, 'Login.html')
   else:
      pass
def checklogin(request):
  if(request.method == 'POST'):
       #check Pass & UserName
      user= MyRegister2.objects.filter(userName=request.POST['userName'] , password2=request.POST['password2'])
      if(user is not None):
         # context={}
          #context['userName'].user[0].userName
          request.session['userName']=request.POST['userName']
          return HttpResponseRedirect('about')

          #return render(request, 'nv.html')
      else:
          return render(request, 'login.html')





