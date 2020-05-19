from django.shortcuts import render,HttpResponse,redirect
import time
import pymongo

uri = "mongodb://localhost:27017/"
myclient = pymongo.MongoClient(uri)
mydb = myclient['loginsystem']
mycol = mydb['register_register']

def index(request):
    return render(request,'register/index.html')

def signup(request):
    if request.method == 'POST':
        fname = request.POST.get('fname', '')
        lname = request.POST.get('lname', '')
        email = request.POST.get('email', '')
        uname = request.POST.get('uname', '')
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')

        if fname == '' or lname == '' or email == '' or uname == '' or password1 == '' or password2 == '':
            return render(request, 'register/index.html', {'message' : "Message: one or more field is empty!"})
        snum = ('0','1','2','3','4','5','6','7','8','9','`','~','!','@','#','$','%','^','&','*','(',')','_','-','+','=')
        for name in [fname, lname]:
            for i in name:
                if i in snum:
                    return render(request, 'register/index.html', {'message' : "Use only alphabets in first and last name!"})
        if password1 == password2:
            count = 0
            for c in password1:
                count +=1
            if count >= 8:
                x = mycol.find_one({'uname': uname})
                if x == None:
                    id = mycol.count_documents({})
                    id = id+1
                    reg_doc ={'id' : id, 'fname' : fname, 'lname' : lname, 'email' : email, 'uname' : uname, 'password1' : password1, 'password2' : password2, 'lastlogin' : time.asctime(time.localtime())}
                    print(reg_doc)
                    mycol.insert_one(reg_doc)
                    return render(request, 'register/index.html', {'message': "Registration successfully done!"})
                else:
                    return render(request, 'register/index.html', {'message' : "User name already exist!"})
            else:
                return render(request, 'register/index.html', {'message' : "Password has atleast 8 characters!"})

        else:
            return render(request, 'register/index.html', {'message' : "Confirm password not same!"})

    return render(request, 'register/index.html')