import json
from django import template
from django.urls import reverse
from django.template.loader import render_to_string
from django.http import JsonResponse
import json
from django.utils.datastructures import MultiValueDictKeyError

from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404, redirect
from django.template.context import RequestContext

from django.shortcuts import render
import pyrebase
import firebase_admin
from django.shortcuts import render
import pyrebase


config = {

    "apiKey": "AIzaSyDfixuOimbjkmTon7lUJrJuLaYicxsYwAY",
  "authDomain": "digonistic.firebaseapp.com",
  "databaseURL": "https://digonistic-default-rtdb.firebaseio.com",
  "projectId": "digonistic",
  "storageBucket": "digonistic.appspot.com",
  "messagingSenderId": "564827073540",
  "appId": "1:564827073540:web:1ec9a2c162e64823599951",
  "measurementId": "G-2PV2NLV99C"
};

# Initialising database,auth and firebase for further use
firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()


def signIn(request):
    return render(request, "sign-in.html")


def dashboard(request):
    y = database.child("silkcity").child("sales and clients").get().val()
    if y==None:
        return render(request, "sign-in.html")
    todaysclient = y["Todaysclient"]
    Todayspatient = y["Todaysmoney"]
    name = y["name"]
    newpatient = y["newpatient"]
    totalmoney = y["totalmoney"]
    totalpatientchart = y["totalpatientchart"]
    dailysales = y["dailysales"]
    patientincreased = y["patientincreased"]

    context = {
        "todaysclient": todaysclient,
        "Todayspatient": Todayspatient,
        "name": name,
        "newpatient": newpatient,
        "totalmoney": totalmoney,
        "totalpatientchart": totalpatientchart,
        "dailysales": dailysales,
        "patientincreased": patientincreased,
    }
    return render(request, "dashboard.html",context)


def postsignIn(request):
    email = request.POST.get('email')
    pasw = request.POST.get('pass')
    try:
        # if there is no error then signin the user with given email and password
        user = authe.sign_in_with_email_and_password(email, pasw)
    except:
        message = "Invalid Credentials!!Please ChecK your Data"
        return render(request, "sign-in.html", {"message": message})
    session_id = user['idToken']
    request.session['uid'] = str(session_id)
    # Get a reference to the database service
    db = firebase.database()
    y=database.child("silkcity").child("sales and clients").get().val()
    todaysclient=y["Todaysclient"]
    Todayspatient=y["Todaysmoney"]
    name=y["name"]
    newpatient=y["newpatient"]
    totalmoney=y["totalmoney"]
    totalpatientchart=y["totalpatientchart"]
    dailysales=y["dailysales"]
    patientincreased=y["patientincreased"]


    context = {
        "todaysclient": todaysclient,
        "Todayspatient":Todayspatient,
        "name":name,
        "newpatient":newpatient,
        "totalmoney":totalmoney,
        "totalpatientchart":totalpatientchart,
        "dailysales":dailysales,
        "patientincreased":patientincreased,
    }
    return render(request, "dashboard.html",context)


def logout(request):
    try:
        del request.session['uid']
    except:
        pass
    return render(request, "Login.html")


def signUp(request):
    return render(request, "sign-up.html")


def postsignUp(request):
    email = request.POST.get('email')
    passs = request.POST.get('pass')
    name = request.POST.get('name')
    try:
        # creating a user with the given email and password
        email="rashedhasanai@gmail.com"
        passs="rostugbot007"
        user = authe.create_user_with_email_and_password(email, passs)
        uid = user['localId']
        idtoken = request.session['uid']
        print(uid)
    except:
        return render(request, "sign-up.html")
    return render(request, "sign-in.html")

def Login(request):
    return render(request,'sign-in.html')
def signup(request):
    return render(request,'sign-up.html')

def billing(request):
    test = database.child("silkcity").child("doctor").get().val()
    d=""
    for key, value in test.items():
        d=d+("-"+str(value['name']))
    my_list =d
    my_dict = dict()
    for index, value in enumerate(my_list):
        my_dict[index] = value
    print(d)
    context = {'my_dict':d}

    return render(request,'billing.html',context)
def postserial(request):
    name = request.POST.get('Name')
    phone = request.POST.get('Phone')
    address=request.POST.get('Address')
    referred=request.POST.get('myCountry')
    status = request.POST.get('status')

    if status=="1":
        status1="new patient"
    elif status=="2":
        status1="old patient"
    else:
        None
    print(name,phone,referred)
    import random
    uid = random.randint(1000000000, 9999999999)
    data = {
        "name": name,
        "phone":phone,
        "address":address,
        "referred":referred,
        "status":status1,
        "UID":uid
    }
    import time

    named_tuple = time.localtime()  # get struct_time
    time_string = time.strftime("%m%d%Y", named_tuple)
    y = database.child("silkcity").child("sales and clients").get().val()
    todaysclient = y["Todaysclient"]
    test = database.child("silkcity").child("doctor").get().val()
    request.session['namepatient'] = name
    request.session['datepatient'] = time_string
    request.session['referredpatient'] = referred
    request.session['uidpatient'] = uid
    for key, value in test.items():
        if value['name']==referred:
            fee=value['fee']

            Todaysmoney = y["Todaysclient"]
            t = y["Todaysmoney"]
            print(Todaysmoney,fee)
            p=int(fee)+int(Todaysmoney)
            q=t+1
            print(p)
            database.child("silkcity").child("sales and clients").update({"Todaysclient":p})
            database.child("silkcity").child("sales and clients").update({"Todaysmoney": q})
    print("date" + str(time_string))

    database.child("silkcity").child("patient").child(referred).child("date" + str(time_string)).child("patients").push(data)
    database.child("silkcity").child("patient").child(uid).push(data)
    return render(request,'billing.html')
def table(request):
    from firebase import firebase
    firebase=firebase.FirebaseApplication('https://digonistic-default-rtdb.firebaseio.com/')

    test = firebase.get('silkcity', '')



    import datetime
    date="02-11-2022"
    doctor = request.POST.get('myCountry')
    date = request.POST.get('date')
    try:
        d = datetime.datetime.strptime(date, '%Y-%m-%d')
        y="date"+str(d.strftime('%m%d%Y'))
    except:
        None

    #print(y,doctor)
    try:
        test = database.child("silkcity").child("patient").child(doctor).child(y).get().val()
    except:
        None
    return render(request, 'tables.html', test)

    print(len(database.child("silkcity").child("patient").get().val()))
    return render(request,'tables.html',test)
def doctor(request):

    test = database.child("silkcity").get().val()
    return render(request,'doctor.html',test)
def adoctor(request):
    return render(request, 'adddoctor.html')
def adddoctor(request):
    doctorname = request.POST.get('doctorName')
    position = request.POST.get('position')
    fee = request.POST.get('fee')
    time = request.POST.get('time')
    print(time, doctorname, fee, position)
    data = {
        "name": doctorname,
        "position": position,
        "fee": fee,
        "time": time
    }
    database.child("silkcity").child("doctor").push(data)

    f=database.child("silkcity").child("doctor").get().val()
    print(len(f))
    f=len(f)
    database.child("silkcity").child("doctorlist").child(f).set(doctorname)
    return render(request, 'adddoctor.html')

def deletedoc(request,docid):
    print(docid)
    import firebase
    test = database.child("silkcity").child("doctor").get().val()
    for key, value in test.items():
        if value['name']==docid:
            database.child("silkcity").child("doctor").child(key).remove()
    return redirect('doctor')
def slip(request):

    name=request.session.get('namepatient')
    date=request.session.get('datepatient')
    referred=request.session.get('referredpatient')
    uid=request.session.get('uidpatient')
    data = {
        "name":name,
        "date":date,
        "referred":referred,
        "uid":uid
    }


    return render(request, 'slip.html',data)
def billpay(request):
    return render(request,'testbilling.html')






def testinfo(request):
    if request.POST.get("form_type") == 'testinfo':
        testname = request.POST.get('testname')
        fee= request.POST.get('fee')
        print(testname, fee)
        data = {
            "testname": testname,
            "fee": fee,
        }
        database.child("silkcity").child("test").push(data)
    test = database.child("silkcity").get().val()
    return render(request,'testinfo.html',test)


def deletetest(request,docid1):
    print(docid1)
    import firebase
    test = database.child("silkcity").child("test").get().val()
    for key, value in test.items():
        if value['testname']==docid1:
            database.child("silkcity").child("test").child(key).remove()
    return redirect('testinfo')





def paystatement(request):
    if request.POST.get("form_type") == 'formTwo':
        testname = request.POST.get('test-name')
        import time

        named_tuple = time.localtime()  # get struct_time
        time_string = time.strftime("%m%d%Y", named_tuple)
        print(testname)
        test = database.child("silkcity").child("test").get().val()
        for key, value in test.items():
            if value['testname'] == testname:
                fee = value['fee']
                print(fee)
        import json
        with open('id.json', 'r') as f:
            data= json.load(f)
        uid=data['uid']
        data={
            "testname":testname,
            "fee":fee
        }

        database.child("silkcity").child("testall").child(uid).child("date" + str(time_string)).child("alltest").push(data)
        data=database.child("silkcity").child("testall").child(uid).child("date" + str(time_string)).get().val()

        return render(request, 'testbilling.html', data)
    if request.POST.get("form_type") == 'formOne':
        uid = request.POST.get('serialnumber')
        print(uid)
        copy= request.POST.copy()
        print("copy",copy['serialnumber'])
        import json

        with open('id.json', 'r') as f:
            data = json.load(f)
            data['uid']=uid
        with open('id.json', 'w') as json_file:
            json.dump(data, json_file)
        print(data)
        import time

        named_tuple = time.localtime()  # get struct_time
        time_string = time.strftime("%m%d%Y", named_tuple)
        test = database.child("silkcity").child("patient").child(uid).get().val()
        for key, value in test.items():
            name=value['name']
            address=value['address']
            phone=value['phone']
            referred=value['referred']
            uid=value['UID']
        data={
            "name":name,
            "address":address,
            "phone":phone,
            "referred":referred,
            "uid":uid
        }
        database.child("silkcity").child("testall").child(uid).child("date"+str(time_string)).child("info").push(data)
        test = database.child("silkcity").child("testall").child(uid).child("date"+str(time_string)).get().val()
        return render(request, 'testbilling.html',test)

    # Handle Elements from first Form
    return render(request, 'testbilling.html')
