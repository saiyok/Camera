from django.shortcuts import render, redirect
from django.http import HttpResponse # คือมีการส่งข้อความตอบกลับ ต้องfrom http เข้ามาทำงาน
from django.contrib.auth.models import User,auth # เวลาที่เราจะบันทึกขึ้นมูลที่เกี่ยวข้องกับ models user ต้อง from และ import อันนี้
from django.contrib import messages  #คือการนำข้อความไปแสดงที่ถ้าเว็บเลย ในที่นี้คือเป็นข้อความ errror
# Create your views here.
def hello(request):
   #return HttpResponse("<h2>Hello non</h2>") #ตัวอักษรหน้าเว็บ
   #return render(request,'index.html') # การดึกข้อมูลจาก html ออกไป
   week = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saterday','Sunday']
   remaining = 0
   return render(request,'index.html',
   {
       'name':'ภัคพงศ์ปณต',
       'number_Camera':'001',
       'week': week,
       'remaining':remaining
   })

def page1(request):
   return render(request,'page1.html')

def page_help(request):
   return render(request,'page_help.html')

def addHelp(request):
   IDname = request.POST['id-code']
   content = request.POST['content']
   return render(request,'result.html',
   {
      'IDname':IDname,
      'content':content
   })

def Table(request):
    return render(request,'Table.html')

def register(request):
   return render(request,'register.html')

def addregister(request):
    StudentID = request.POST['StudentID']
    FirstName = request.POST['FirstName']
    LastName = request.POST['LastName']
    Email = request.POST['Email']
    Password = request.POST['Password']
    RePassword = request.POST['RePassword']

    if Password == RePassword:
        if User.objects.filter(username= StudentID).exists(): # เช็คว่ามี  username ในฐานข้อมูลที่ซึ่ากันหรือเปล่า
            messages.info(request,'Student ID นี้มีผู้ใช้แล้ว')
            #print("repeatedly username")
            return redirect('/register')
        elif User.objects.filter(email = Email).exists():
            messages.info(request,'Email นี้มีผู้ใช้แล้ว')
            return redirect('/register')
        else:

            user = User.objects.create_user(    #การนำข้อมูลไปเก็บในตาราง user
            username= StudentID,
            first_name= FirstName,
            last_name= LastName,
            email = Email,
            password = Password
            )
            user.save()
            return render(request,'result.html')
    else:
        messages.info(request,'Password ไม่ตรงกัน')
        return redirect('/register')
        

def loginForm(request):
    return render(request,'login.html')

def login(request):
    StudentID = request.POST['StudentID']
    Password = request.POST['Password']

    #login (check username,passwork)
    user = auth.authenticate(username=StudentID,password=Password)

    if user is not None:
        auth.login(request,user)
        return redirect('/BorrowBack')

    else:
        messages.info(request,'ข้อมูลไม่ถูกต้อง')
        return redirect('/loginForm')


def logout(request):
    auth.logout(request)
    return redirect('/loginForm')

def BorrowBack(request):
    return render(request,'BorrowBack.html')

def RanNumBR(request):
    return render(request,'RanNumBR.html')

def RanNumBack(request):
    return render(request,'RanNumBack.html')
