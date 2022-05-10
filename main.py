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

#email=str(input())
#passs=str(input())
#authe.sign_in_with_email_and_password(email,passs)
#authe.create_user_with_email_and_password()
#storage=firebase.storage()
#filename=input()
#cloudname=input()
#storage.child(cloudname).put(filename)
#print(storage.child(cloudname).get_url(None))
data={
  "name":"rashed"
}
database.child("silkcity").child("1st").push(data)
e=database.child("silkcity").child("patient").get(data).val()
#database.child("silkcity").child("1st").update({"name":"nayem"})
test=database.child("silkcity").get().val()
print(len(e))

