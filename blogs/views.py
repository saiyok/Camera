from django.shortcuts import render, redirect
from django.http import HttpResponse # คือมีการส่งข้อความตอบกลับ ต้องfrom http เข้ามาทำงาน
from django.contrib.auth.models import User,auth # เวลาที่เราจะบันทึกขึ้นมูลที่เกี่ยวข้องกับ models user ต้อง from และ import อันนี้
from django.contrib import messages  #คือการนำข้อความไปแสดงที่ถ้าเว็บเลย ในที่นี้คือเป็นข้อความ errror

from random import randrange
import pymysql
import json
# Create your views here.
def connect_db():
    con = pymysql.connect(host='localhost',
                          user='root',
                          password='a',
                          db='pj_camera')
    return con

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
            db = connect_db()
            try:
                cursor = db.cursor()
                cursor.execute(insert_sql('info', data))
                db.commit()
            except:
                print('error')
            db.close()

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
 
def key_Num(request):
    return render(request,'key_Num.html')


def insert_sql(table_name, value_json):
    print('difeijofpajnvgirgjnj')
    sql = ""
    if table_name == 'info':
        sql = "INSERT INTO `info` (`ID`, `PASSWORD`, `NAME`, `STATUS`, `CAMERA_ID`, `TIME`) \
         VALUES ('%d', '%d', '%s', '%d', '%d', '%d')" % \
              (value_json["id"], value_json["password"], value_json["name"], value_json["status"], value_json["camera_id"],value_json["time"])
    elif table_name == 'user_info':
        sql = "INSERT INTO `user_info` (`ID`, `LAST_ACTION`, `HISTORY`, `REPORT`, `PERSONAL`) \
         VALUES ('%d', '%s', '%s', '%s', '%s')" %\
              (value_json["id"],value_json['last_action'],value_json["history"],value_json['report'],value_json["personal"])
    return sql



with open("data.json", 'r') as f:
    data = json.load(f)
    data = data["user_id"]["1"]

# {
#   "user_id": {
#     "1": {
#       "id": 123456,
#       "password": 123256,
#       "name": 'Ryujin Jakra ภูเขาไฟ',
#       "status": 2,
#       "camera_id": 102030,
#       "time": 10.00,
#       "last_action": 2,
#       "history":  2,
#       "report": 2,
#       "personal": {
#         "age": 2,
#         "sex": "male"
#       }
#     },
#     "2": {
#       "id": 123456,
#       "password": 123256,
#       "name": 'Ryujin Jakra ภูเขาไฟ',
#       "status": 2,
#       "camera_id": 102030,
#       "time": 10.00,
#       "last_action": 2,
#       "history":  2,
#       "report": 2,
#       "personal": {
#         "age": 2,
#         "sex": "male"
#       }
#     }
#   }
# }





# with open("data.json", "r") as read_file:
#     data = json.load(read_file)
#     data = data["user_id"]["1"]

