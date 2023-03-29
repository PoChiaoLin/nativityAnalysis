from bs4 import BeautifulSoup
import re
import requests
from django.http import HttpResponse
from django.shortcuts import render
from myapp.models import Dreamreal
# Create your views here.

from django.core.mail import send_mail
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


def sendSimpleEmail(request, emailto):
    res = send_mail("hello Allen", "comment tu vas?",
                    "allenkuo0720@gmail.com", [emailto])
    return HttpResponse('%s' % res)


def signIn(request):
    return render(request, "firebaseLogin.html")


def home(request):
    return render(request, "firebaseHome.html")


def postsignIn(request):
    email = request.POST.get('email')
    pasw = request.POST.get('pass')
    try:
        res = send_mail("hello Allen", "comment tu vas?",
                        "allenkuo0720@gmail.com", [email])
        return HttpResponse('%s' % res)
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


def postsignUp(request):
    email = request.POST.get('email')
    passs = request.POST.get('pass')
    name = request.POST.get('name')

    res = send_mail("hello Allen", "comment tu vas?",
                    "allenkuo0720@gmail.com", [email])
    return HttpResponse('%s' % email)

    try:
        send_mail("hello Allen", "comment tu vas?",
                  "allenkuo0720@gmail.com", [email, 'allenkuo0720@gmail.com'])
        print(email)
        # creating a user with the given email and password
        user = authe.create_user_with_email_and_password(email, passs)
        uid = user['localId']
        idtoken = request.session['uid']
        print(uid)
        # send_mail("hello Allen", "comment tu vas?",
        #           "allenkuo0720@gmail.com", [email, 'allenkuo0720@gmail.com'])

    except:
        return render(request, "firebaseRegistration.html")
    return render(request, "firebaseLogin.html")


def crudops(request):
    # Creating an entry

    dreamreal = Dreamreal(
        website="www.google.com",
        mail="alvin@google.com.com",
        name="alvin",
        phonenumber="0911222333"
    )

    dreamreal.save()

    # Read ALL entries
    objects = Dreamreal.objects.all()
    res = 'Printing all Dreamreal entries in the DB : <br>'

    for elt in objects:
        res += elt.name + "<br>"

    # Read a specific entry:
    sorex = Dreamreal.objects.get(name="alvin")
    res += 'Printing One entry <br>'
    res += sorex.name

    # Delete an entry
    res += '<br> Deleting an entry <br>'
    sorex.delete()

    # Update
    dreamreal = Dreamreal(
        website="www.google.com",
        mail="alvin@google.com.com",
        name="alvin",
        phonenumber="0911222444"
    )

    dreamreal.save()
    res += 'Updating entry<br>'

    dreamreal = Dreamreal.objects.get(name='alvin')
    dreamreal.name = 'mary'
    dreamreal.save()

    return HttpResponse(res)


def viewArticles(request, year, month):
    text = "Displaying articles of : %s/%s" % (year, month)
    return HttpResponse(text)


def viewArticle(request, articleId):
    """ A view that display an article based on his ID"""
    text = "Displaying article Number : %s" % articleId
    return redirect("hello2")


def lotto(year, month):
    myHeaders = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}

    r = requests.get(
        'https://www.taiwanlottery.com.tw/lotto/superlotto638/history.aspx', headers=myHeaders)
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'html.parser')
        __VIEWSTATEGENERATOR = soup.select_one(
            'input#__VIEWSTATEGENERATOR').get('value')
        __EVENTVALIDATION = soup.select_one(
            'input#__EVENTVALIDATION').get('value')
        __VIEWSTATE = soup.select_one('input#__VIEWSTATE').get('value')

    # for year in range(103, 113):
        # for month in range(1, 13):

    myData = {'__VIEWSTATEGENERATOR': __VIEWSTATEGENERATOR,
              '__EVENTVALIDATION': __EVENTVALIDATION,
              '__VIEWSTATE': __VIEWSTATE,
              '__VIEWSTATEENCRYPTED': '',
              '__EVENTTARGET': '',
              '__EVENTARGUMENT': '',
              '__LASTFOCUS': '',
              'forma': '請選擇遊戲',
              'SuperLotto638Control_history1$chk': 'radYM',
              'SuperLotto638Control_history1$dropYear': year,
              'SuperLotto638Control_history1$dropMonth': month,
              'SuperLotto638Control_history1$btnSubmit': '查詢'}

    r = requests.post(
        'https://www.taiwanlottery.com.tw/lotto/superlotto638/history.aspx', headers=myHeaders, data=myData)
    r.encoding = 'utf-8'
    if r.status_code == 200:
        # print(r.text)

        soup = BeautifulSoup(r.text, 'html.parser')
        num = soup.find_all('span', id=re.compile(
            'SuperLotto638Control_history1_dlQuery_DrawTerm_\d'))
        number = soup.find_all('span', id=re.compile(
            'SuperLotto638Control_history1_dlQuery_SNo\d_\d'))

        result = ""
        for index, n1 in enumerate(number):
            if (index) % 7 == 0:
                # print(num[index//7].text+":", end=' ')
                result = result + num[index//7].text + ":" + " "
            # print(n1.text, end=' ')
            result = result + n1.text + " "
            if (index+1) % 7 == 0:
                # print()
                result = result + "<br>"
    return result


def index(request):
    return render(request, "index.html", locals())           # 此行有渲染網頁(法2)


def login(request):
    user = request.POST.get('user')
    password = request.POST.get('password')
    # 測試用！！(寫後端時，最好的測試就是把結果打到前端)
    return HttpResponse(user + password)
    # return render(request, "index.html", locals())           # 此行有渲染網頁(法2)


def hello(request):
    # text = "hello allen123"                                # 此行&下一行單純把字打到前端，沒有渲染網頁(法1)
    # return HttpResponse(text)
    return render(request, "hello.html", {"name": "allen"})  # 此行有渲染網頁(法2)


def hello1(request, number):                                 # 此為位置對應法
    # text = "hello allen123"
    # return HttpResponse(text)
    return render(request, "hello.html", {"name": number})


def hello2(request):                                         # 此為名稱對應法
    # text = "hello allen123"
    # return HttpResponse(text)
    number = request.GET.get('number')
    # request.args.Get('number')是flask的寫法，django要改成request.GET.get('number')；若要用post，則把GET改成POST(全大寫)
    score = request.GET.get('score')
    # return render(request, "hello2.html", {"number": number, "score": score})
    # 上一行亦可改成下一行的寫法
    return render(request, "hello2.html", locals())


def getLotto(request):
    year = "105"
    month = "6"
    return HttpResponse(lotto(year, month))
