from django.shortcuts import render

# Create your views here.

import pyrebase
from random import randint
from django.core.mail import send_mail

import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth

config = {
    'apiKey': "AIzaSyAj7-2jI9QADY0HSNO9Eh4kEGWnmgWqYQY",
    'authDomain': "django-8words.firebaseapp.com",
    'databaseURL': "https://django-8words-default-rtdb.firebaseio.com",
    'projectId': "django-8words",
    'storageBucket': "django-8words.appspot.com",
    'messagingSenderId': "367449997168",
    'appId': "1:367449997168:web:96edec47ab472ed7a359b5",

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


otp = randint(000000, 999999)


def postsignUp(request):
    email = request.POST.get('email')
    passs = request.POST.get('pass')
    name = request.POST.get('name')
    # try:
    # otp = randint(000000, 999999)

    # msg = Message('OTP', sender='allenkuo0720@gmail.com', recipients=[email])
    # msg.body = "This is your one-time OTP number:"+str(otp)
    # mail.send(msg)

    # return render(request, "verify.html")

    # creating a user with the given email and password
    user = authe.create_user_with_email_and_password(email, passs)
    uid = user['localId']
    # idtoken = request.session['uid']
    print(uid)

    dict1 = {"email": email}

    database.child('Humandata').push(dict1)

    message = "This is your one-time OTP number:"+str(otp)
    send_mail("帳號驗證", message,
              "allenkuo0720@gmail.com", [email, 'allenkuo0720@gmail.com'])

    # except:
    # message = "本帳號已存在，請確認！！"
    # return render(request, "firebaseLogin.html", {"message": message})
    # except:
    # return render(request, "failure.html")
    # return render(request, "firebaseLogin.html")
    return render(request, "verify.html")


def validate(request):
    user_otp = request.POST.get('otp')
    # return user_otp
    if otp == int(user_otp):
        return render(request, "birthday.html")
    # return render(request, "success.html")
    else:
        return render(request, "firebaseRegistration.html")


def birthdaysave(request):
    email = database.child('Humandata').child('email').get().val()
    year = request.POST.get('Year')
    month = request.POST.get('Month')
    day = request.POST.get('Day')
    time = request.POST.get('Time')
    gender = request.POST.get('Gender')

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

    dict2 = {"year": year, "month": month,
             "day": day, "time": time, "gender": gender}
    database.child('Humandata').child('email').push(dict2)
    # database.child('Humandata').child('Year').push(year)
    # database.child('Humandata').child('Month').push(month)
    # database.child('Humandata').child('Day').push(day)
    # database.child('Humandata').child('Time').push(time)
    # database.child('Humandata').child('Gender').push(gender)

    year = database.child('Humandata').child('Year').get().val()
    month = database.child('Humandata').child('Month').get().val()
    day = database.child('Humandata').child('Day').get().val()
    time = database.child('Humandata').child('Time').get().val()
    gender = database.child('Humandata').child('Gender').get().val()
    return render(request, "birthdaysave.html", {"year": year, "month": month, "day": day, "time": time, "gender": gender})
