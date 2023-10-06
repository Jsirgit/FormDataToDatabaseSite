import email
from unicodedata import name
from django.shortcuts import render,HttpResponseRedirect
from . forms import StudentR
from . models import FormData

# Create your views here.


def showformdata(request):
    if request.method == 'POST':
        fm = StudentR(request.POST)
        if fm.is_valid():
            print('form Validated')
        name = fm.cleaned_data['name']
        email = fm.cleaned_data['email']
        password = fm.cleaned_data['password']
        print('Name:', name)
        print('Email:', email)
        print('Password:', password)
        FormData.objects.create(name=name, email=email, password=password)
        return render(request, 'enroll/success.html', {'nm':name})
        # print('Yeh POST Request se Aaya hai')
        # print('Clean Data', fm.cleaned_data)
    else:
        fm = StudentR()
        # print('Yeh get Request se Aaya hai')
        return render(request, 'enroll/userr.html',{'form': fm})

def thankyou(request):
   return render(request, 'enroll/success.html')
