from django.shortcuts import *
from pymongo import MongoClient


client=MongoClient("mongodb://localhost:27017/")
db=client["user"]
collection=db["register"]

def registeration(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        collection.insert_one({
            "username":username,
            "password":password
        })
        return redirect(login)
    return render(request,"register.html")    

def login(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=collection.find_one({"username":username,"password":password})
        if user:
            request.session["username"]=username
            return redirect(userpage)
        else:
            return render(request, "login.html")
    return render(request, "login.html")



def logout(request):
   return redirect(login)


def userpage(request):
    username=request.session.get("username")  
    if username:
        return render(request,"userpage.html",{"username":username})
    else:
        return render(request,"login.html")

