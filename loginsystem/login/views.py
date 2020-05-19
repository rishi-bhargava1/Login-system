from django.shortcuts import render, redirect
import time
import pymongo

uri = "mongodb://localhost:27017/"
myclient = pymongo.MongoClient(uri)
mydb = myclient['loginsystem']
mycol = mydb['register_register']
print("in login views")
def index(request):
    return render(request, 'login/index.html')

def signin(request):
    if request.method == 'POST':
        uname = request.POST.get('uname', '')
        password = request.POST.get('password', '')

        if uname == '' or password == '':
            return render(request, 'login/index.html', {'message' : 'Message: One or more field is empty!' })

        user_doc = mycol.find_one({'uname' : uname, 'password1' : password})

        if user_doc == None:
            return render(request, 'login/index.html', {'message': 'Message: Not valid user!'})
        else:
            mycol.update_one({'uname' : uname}, {'$set' : {'lastlogin' : time.asctime(time.localtime())}})
            return render(request, 'web.html', {'message' : uname})
            # return redirect('web')

    return render(request, 'login/index.html')