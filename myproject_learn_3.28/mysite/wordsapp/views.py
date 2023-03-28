import base64  # 新增
from django.core import signing  # 新增
from django.core.mail import send_mail  # 新增
# from IThome_Django import settings  # 新增
from datetime import datetime
from django.contrib.sessions.models import Session
from django.contrib import auth
# from user.models import UserProfile
from django.views.decorators.csrf import csrf_protect
from django.http.response import JsonResponse
from django.contrib.auth.models import User
import uuid
import json
from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.
import pyrebase

config = {
    'apiKey': "AIzaSyAj7-2jI9QADY0HSNO9Eh4kEGWnmgWqYQY",
    'authDomain': "django-8words.firebaseapp.com",
    'databaseURL': "https://django-8words-default-rtdb.firebaseio.com",
    'projectId': "django-8words",
    'storageBucket': "django-8words.appspot.com",
    'messagingSenderId': "367449997168",
    'appId': "1:367449997168:web:96edec47ab472ed7a359b5"

}

firebase = pyrebase.initialize_app(config)
database = firebase.database()


def index(request):
    return render(request, "index.html", locals())           # 此行有渲染網頁(法2)


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


# from IThome_Django import settings #新增


class email_token():
    def __init__(self):
        self.salt = str(base64.encodestring(bytes("1_23a48c9710295", "utf-8")))

    def generate_token(self, email):
        signer = signing.TimestampSigner(salt=self.salt).sign_object(email)
        return signer


def postsignUp(request):
    try:
        email = request.POST.get('email')
        passs = request.POST.get('pass')
        name = request.POST.get('name')
        message = "\n".join(["{0}歡迎使用app".format(name),
                             "請點選下列連結完成註冊:\n",
                             "/".join(['127.0.0.1:8000/wordsapp/', token_s])])
        send_mail("帳號驗證", message,
                  "allenkuo0720@gmail.com", [email, 'allenkuo0720@gmail.com'])

        message = {'status': '0', "token": token_s}
        user = authe.create_user_with_email_and_password(email, passs)
        uid = user['localId']
        idtoken = request.session['uid']
        print(uid)
    except:
        message = {'status': '1'}

    # send_mail("hello Allen", "comment tu vas?",
    #           "allenkuo0720@gmail.com", [email, 'allenkuo0720@gmail.com'])
    # try:
    #     # creating a user with the given email and password
    #     user = authe.create_user_with_email_and_password(email, passs)
    #     uid = user['localId']
    #     idtoken = request.session['uid']
    #     print(uid)
    # except:
    #     return render(request, "firebaseRegistration.html")
    return render(request, "firebaseLogin.html")
