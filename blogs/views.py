from django.shortcuts import render
from django.http import HttpResponse # คือมีการส่งข้อความตอบกลับ ต้องfrom http เข้ามาทำงาน
from django.contrib.auth.models import User # เวลาที่เราจะบันทึกขึ้นมูลที่เกี่ยวข้องกับ models user ต้อง from และ import อันนี้
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
    PhoneNumber = request.POST['PhoneNumber']
    Password = request.POST['Password']
    RePassword = request.POST['RePassword']

    User.object.create_user(
        username= StudentID,
        first_name= FirstName,
        last_name= LastName
        
    )
    return render(request,'result.html')


  