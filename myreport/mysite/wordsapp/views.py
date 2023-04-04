from django.shortcuts import render, redirect  # ,徐尉庭增加 redirect
from django.contrib.auth import update_session_auth_hash  # 徐尉庭增加
from django.contrib.auth.forms import PasswordChangeForm  # 徐尉庭增加
from .crawler import 生辰八字主業  # 徐尉庭增加
# Create your views here.
import re
import pyrebase
from random import randint
from django.core.mail import send_mail

import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
from firebase_admin import db

config = {
    'apiKey': "AIzaSyD34Ag5lIY3rqWx-JxxpnlRWHFH89Yz_Fw",
    'authDomain': "django-8words-2c6a1.firebaseapp.com",
    'databaseURL': "https://django-8words-2c6a1-default-rtdb.firebaseio.com",
    'projectId': "django-8words-2c6a1",
    'storageBucket': "django-8words-2c6a1.appspot.com",
    'messagingSenderId': "214881135592",
    'appId': "1:214881135592:web:933d120422cab3dd13925d",

    # 'apiKey': "AIzaSyAj7-2jI9QADY0HSNO9Eh4kEGWnmgWqYQY",
    # 'authDomain': "django-8words.firebaseapp.com",
    # 'databaseURL': "https://django-8words-default-rtdb.firebaseio.com",
    # 'projectId': "django-8words",
    # 'storageBucket': "django-8words.appspot.com",
    # 'messagingSenderId': "367449997168",
    # 'appId': "1:367449997168:web:96edec47ab472ed7a359b5",

}

firebase = pyrebase.initialize_app(config)
database = firebase.database()


def fireBaseDBtest(request):

    day = database.child('Data').child(
        'Day').get().val()              # .child()就是往下一層
    id = database.child('Data').child('Id').get().val()
    projectname = database.child('Data').child('ProjectName').get().val()

    # database.child("Data").child("Morty")

    # data = {"name": "Mortimer 'Morty' Smith"}
    # database.child("Data").push(data)

    # data = {"name": "Mortimer 'Morty' Smith"}
    # database.child("Data").child("Morty").set(data)

    # database.child("Data").child("Morty").update({"name": "Mortiest Morty"})

    # database.child("Data").child("Morty").remove()

    # data = {
    #     "Data/Morty/": {"name": "Mortimer 'Morty' Smith"},
    #     "Data/Rick/":  {"name": "Rick Sanchez"}
    # }
    # database.update(data)

    # data = {
    #     "Data/" + database.generate_key(): {"name": "Mortimer 'Morty' Smith"},
    #     "Data/" + database.generate_key(): {"name": "Rick Sanchez"}
    # }
    # database.update(data)

    # data = database.child("Data").get()

    # print(data.val())

    # data = database.child("Data").get()

    # print(data.key())

    # all_Data = database.child("Data").get()

    # for data in all_Data.each():
    #     print(data.key())

    #     print(data.val())

    return render(request, "fireBaseDBtest.html", {"day": day, "id": id, "projectname": projectname})
    # return HttpResponse("done")


authe = firebase.auth()


def signIn(request):
    return render(request, "firebaseLogin.html")


def home(request):
    return render(request, "firebaseHome.html")


def postsignIn(request):
    email = request.POST.get('email')
    pasw = request.POST.get('pass')
    try:
        # if there is no error then signin the user with given email and password
        user = authe.sign_in_with_email_and_password(email, pasw)
    except:
        message = "Invalid Credentials!!Please Check your Data"
        return render(request, "firebaseLogin.html", {"message": message})
    session_id = user['idToken']
    request.session['uid'] = str(session_id)
    return render(request, "firebaseHome.html", {"email": email})


def logout(request):
    try:
        del request.session['uid']
    except:
        pass
    return render(request, "firebaseLogin.html")


def signUp(request):
    return render(request, "firebaseRegistration.html")


# otp = randint(000000, 999999)

# globalemail = ""

def otpVerify(email, passs, request):
    otp = randint(000000, 999999)
    try:
        user = authe.create_user_with_email_and_password(email, passs)
        uid = user['localId']
        dict1 = {"otp": otp, "email": email}
        a = email.split('.')
        database.child('Humandata').child(a[0]).push(dict1)
        database.child("email_t").push(a[0])
        ref = db.reference('email_t')
        datas = ref.get()
        for b in datas.keys():
            if datas[b] == a[0]:
                value = datas[b]
                ref.child(value).set(value)
                ref.child(b).delete()
        ref = db.reference('email_t')
        datas = ref.get()
        for b in datas.keys():
            if datas[b] == a[0]:
                value = datas[b]
                ref.child(value).set(value)
                ref.child(b).delete()
        message = "This is your one-time OTP number:"+str(otp)
        send_mail("帳號驗證", message,
                  "allenkuo07201@gmail.com", [email, 'allenkuo07201@gmail.com'])
    except:
        message = "本帳號已存在，請確認！！"
        return render(request, "firebaseLogin.html", {"message": message})
    return render(request, "verify.html")


def postsignUp(request):
    # global globalemail
    email = request.POST.get('email')
    passs = request.POST.get('pass')
    name = request.POST.get('name')
    otpVerify(email, passs)
    # globalemail = email
    otp = randint(000000, 999999)

    # try:
    # otp = randint(000000, 999999)

    # msg = Message('OTP', sender='allenkuo0720@gmail.com', recipients=[email])
    # msg.body = "This is your one-time OTP number:"+str(otp)
    # mail.send(msg)

    # return render(request, "verify.html")

    # creating a user with the given email and password
    #user = authe.create_user_with_email_and_password(email, passs)
    #uid = user['localId']
    # idtoken = request.session['uid']
    # print(uid)

    # dict1 = {"email": email}
    #dict1 = {"otp": otp, "email": email}
    # database.child('Humandata').child(email.split('@')[0]).push(dict1)
    #a = email.split('.')
    # database.child('Humandata').child(a[0]).push(dict1)

    #message = "This is your one-time OTP number:"+str(otp)
    # send_mail("帳號驗證", message,
    # "allenkuo07201@gmail.com", [email, 'allenkuo07201@gmail.com'])

    # context = {"email": email}

    # except:
    #message = "本帳號已存在，請確認！！"
    # return render(request, "firebaseLogin.html", {"message": message})
    # except:
    # return render(request, "failure.html")
    # return render(request, "firebaseLogin.html")
    # return render(request, "verify.html")


def validate(request):
    # otp = database.child('Humandata').child(email.split('.')[0]).get().val()
    # email_id = database.child('Humandata').get().key()
    import os

    # 获取当前工作目录
    # current_dir = os.getcwd()

    # 构建 Firebase 金钥的绝对路径
    # key_path = os.path.join(
    #     current_dir, 'django-8words-firebase-adminsdk-nok9a-2edc05f7c4.json')

    # email = request.POST.get('email')
    # context = {"email": email}
    # a = email.split('.')

    if not firebase_admin._apps:
        # 設定 Firebase Admin SDK 的認證憑證
        cred = credentials.Certificate(
            'django-8words-2c6a1-firebase-adminsdk-usxvz-3e2e8a279e.json')
        # django-8words-firebase-adminsdk-nok9a-2edc05f7c4
        firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://django-8words-2c6a1-default-rtdb.firebaseio.com/'
        })

    # 取得 Firebase Realtime Database 的根節點
    ref = db.reference('Humandata')

    # 讀取資料
    data = ref.get()
    # print(data)
    email = 0
    otp = 0
    for i in data.values():
        for j in i.values():
            for k in j.values():
                # 這裡要加判斷式len(k)<7就是otp
                otp = int(k)
                # print(k)

    # otp = database.child('Humandata').child(email).get().val()
    # for data in datas.each():
    #     print(data.val())
    user_otp = request.POST.get('otp')

    temp_otp = int(user_otp)
    # return user_otp
    if otp == temp_otp:
        return render(request, "birthday.html")
    # return render(request, "success.html")
    else:  # 加入刪除帳戶的程式碼
        # user.delete()
        return render(request, "firebaseRegistration.html")


def birthdaysave(request):  # 待改
    # email = database.child('Humandata').child(globalemail).get().val()
    born = request.POST.get('birthdate')
    born_split = born.split('-')
    year = born_split[0]
    month = born_split[1]
    day = born_split[2]

    # year = request.POST.get('Year')
    # month = request.POST.get('Month')
    # day = request.POST.get('Day')
    time = request.POST.get('time')
    gender = request.POST.get('gender')

    # # 檢查 Firebase Admin SDK 是否已經初始化
    # if not firebase_admin._apps:
    #     # 設定 Firebase Admin SDK 的認證憑證
    #     cred = credentials.Certificate(
    #         "django-8words-firebase-adminsdk-nok9a-2edc05f7c4.json")

    #     firebase_admin.initialize_app(cred, {
    #         'databaseURL': 'https://django-8words-default-rtdb.firebaseio.com'
    #     })

    # # 取得Firebase Authentication的使用者ID
    # user_id = "user-id"
    # user = auth.get_user(user_id)

    # # 取得使用者的email
    # email = user.email
    # print(email)

    # 取得 Firebase Realtime Database 的根節點
    ref = db.reference('Humandata')

    # 讀取資料
    data = ref.get()

    id = 0
    for u in data.keys():
        id = u
        # print(u)

    dict2 = {"year": year, "month": month,
             "day": day, "time": time, "gender": gender}
    database.child('Humandata').child(id).set(dict2)
    # database.child('Humandata').child('Year').push(year)
    # database.child('Humandata').child('Month').push(month)
    # database.child('Humandata').child('Day').push(day)
    # database.child('Humandata').child('Time').push(time)
    # database.child('Humandata').child('Gender').push(gender)

    # year = database.child('Humandata').child(
    #     email.split('.')[0]).child('Year').get().val()

    year = database.child('Humandata').child(id).child('year').get().val()
    month = database.child('Humandata').child(id).child('month').get().val()
    day = database.child('Humandata').child(id).child('day').get().val()
    time = database.child('Humandata').child(id).child('time').get().val()
    gender = database.child('Humandata').child(id).child('gender').get().val()
    return render(request, "birthdaysave.html", {"year": year, "month": month, "day": day, "time": time, "gender": gender})
# 以下是徐尉庭增加的


def 查詢(request):
    if request.method == 'POST':
        if 'search_horoscope' in request.POST:
            return redirect('birthday')

    return render(request, '查詢.html')


def birthday(request):
    if request.method == 'POST':
        birthdate = request.POST['birthdate']
        time = request.POST['time']
        gender = request.POST['gender']

        # 将birthdate分解为Year, Month, Day
        Year, Month, Day = birthdate.split('-')

        # 调用爬虫函数
        horoscope, nativityAnalysis = 生辰八字主業(Year, Month, Day, time, gender)

        # 将结果传递给模板
        context = {
            'horoscope': horoscope,
            'nativityAnalysis': nativityAnalysis,
        }
        return render(request, 'birth_result.html', context)
    else:
        return render(request, 'birthday.html')
    # 上面為徐尉庭增加
