from django.http import response
from django.shortcuts import redirect, render
#Importing logout for logout function
from django.contrib.auth import logout
from app.models import Users,ContactusDB,adminuser,user_response
from django.contrib import messages

#For uploading files to server we need
from django.core.files.storage import FileSystemStorage
import datetime

# Create your views here.
def home(request):
    #Before calling home ending any use session using logout(request) function this won't through any error
    #if no user has loged in
    logout(request)
    return render(request,'Home.html')

def LogoType(request):
    return render(request,'Logo Type.html')

def ContactUs(request):     
    if request.method == 'POST':
        post=ContactusDB()
        post.cname= request.POST.get('cname')
        post.csubject=request.POST.get('csubject')
        post.cphonenumber=request.POST.get('cphoneno')
        post.cemail=request.POST.get('cemail')
        post.cmsg=request.POST.get('cmsg')
        post.save()
                
        return render(request, 'Contact Us.html')  

    else:
        return render(request,'Contact Us.html')
    

def AboutUs(request):
    return render(request,'AboutUs.html')

def LoginAndSignUp(request):
    if request.method == 'POST':
        post=Users()
        post.username= request.POST.get('username')
        post.umail=request.POST.get('email')
    
        try:
            Users.person.get(umail=post.umail)
            messages.error(request,"Emaill Already Taken")
            return render(request, 'LoginAndSignUp.html') 
        except:    
            post.uphone=request.POST.get('phoneno')
            post.upassword=request.POST.get('password')
            post.uconfirmpass=request.POST.get('uconfirmpassword')
            if(post.upassword!=post.uconfirmpass):
                messages.error(request,"Password and confirm password should be same")
                return render(request, 'LoginAndSignUp.html') 
        
        post.save()
        messages.success(request, 'Your profile was updated.')   
        return render(request, 'LoginAndSignUp.html')  

    else:
        return render(request,'LoginAndSignUp.html')
        

# def AdminSignin(request):
#     return render(request,'AdminLogin.html')

def userDashboard(request):
    if request.method=="POST":
        try:
            # print(request.POST['umail'])
            # print(request.POST['upassword'])
            # user=Users.person.get(umail=request.POST['umail'],upassword=request.POST['upassword'])
            # print(user.umail)
            # print(user.upassword)
            userdetails=Users.person.get(umail=request.POST['umail'],upassword=request.POST['upassword'])
            request.session['Email']=userdetails.umail
            email=request.POST['umail']
            #Requesting session so that we can use it to access it in user profile
            usname=userdetails.username
            return render(request,"userDashboad.html")
        except:
            messages.error(request,'Failed to login No Such User exits')
            return render(request,'LoginAndSignUp.html')
    else:
        email = request.session['Email']
        return render(request,'userDashboad.html')
    

    


# def usercontactusrespond(request):
#     if request.method =="POST":
#         form=UsersForm(request.POST)
#         #Below checking form is valid i.e. all conditions are beimng satisfied or not
#         if form.is_valid():
#             try:
#                 form.save()
#                 return redirect('Login And Sign Up')
#             except:
#                 pass
#              else:


#For chat page
def room(request,room_name):
    return render(request,'chatroom.html', {
        'room_name':room_name,
    })

def Readmore(request):
    return render(request,'Readmore.html')    

def admin(request):
    return render(request,'AdminLogin.html')

    
def userprofile(request):
    email=request.session['Email']
    try:
        userdetails=Users.person.get(umail=email)
        usname=userdetails.username
        upassword=userdetails.upassword
        uphone=userdetails.uphone
        return render(request,"userprofile.html",{'email': email,'name':usname,'password':upassword,'phone':uphone})
    except:
        messages.error(request,'Failed to get data from database!! Please Contact Admin')
        return render(request,'userDashboard.html')

def updateuser(request):
    if request.method=="POST":
        try:
           Users.person.filter(umail=request.POST['email']).update(username=request.POST['name'],upassword=request.POST['password'],uphone=request.POST['phoneno'])
           messages.success(request, 'Your profile was updated uccessfully.')
           #Now to get new contents which are updated from database
           userdetails=Users.person.get(umail=request.POST['email'])
           usname=userdetails.username
           upassword=userdetails.upassword
           uphone=userdetails.uphone
           return render(request,"userprofile.html",{'email': request.POST['email'],'name':usname,'password':upassword,'phone':uphone})
  
        except:
            messages.error(request,'Failed to update user profile')
            #Now to get new contents which are updated from database
            userdetails=Users.person.get(umail=request.POST['email'])
            usname=userdetails.username
            upassword=userdetails.upassword
            uphone=userdetails.uphone
            return render(request,"userprofile.html",{'email': request.POST['email'],'name':usname,'password':upassword,'phone':uphone})
    else:
        print("Method is not POST")


def predictimage(request):
    print(request)
    print(request.POST.dict())
    fileobj=request.FILES['filepath']
    fs=FileSystemStorage()
    filepathname=fs.save(fileobj.name,fileobj)
    filepathname=fs.url(filepathname)
    testimage='.'+filepathname
    from keras.models import load_model
    import cv2
    import numpy as np
    from keras_preprocessing import image


    model = load_model('model/my_model.h5')
    model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])


    # img = cv2.imread('CNN.model/twist institution 14.jpg')
    print(filepathname)
    img = image.load_img(testimage, target_size=(64,64))
    x = image.img_to_array(img)
    x=x/255
    x=x.reshape(1,64,64,3)
    predictions = model.predict(x)
    print(predictions)
    # Generate arg maxes for predictions
    classes = np.argmax(predictions, axis = 1)
    print(classes)


    print(testimage)


    if(classes == 0):
        print("Combination")
        result = "Combination"
    elif(classes==1):
        print("Emblem")  
        result = "Emblem"
    elif(classes==2):
        print("Lettermark")
        result = "Lettermark"
    elif(classes==3):
        print("Wordmark")
        result = "Wordmark"

    #U

   
    return render(request,'modelResult.html',{'testimage':testimage,'result':result})

def adminHome(request):
    #First Getting text from textfield
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']

        # print(username)
        # print(password)
        try:
            admins = adminuser.adminobject.get(username=username,password=password)
            request.session['email'] = admins.email
            name = admins.username
            email=request.session['email']

            #For statistical graphs
            totalimgtested = user_response.userresponse_model_obj.all().count()
            successfultests = user_response.userresponse_model_obj.filter(user_response = "Yes").count()
            failedtests = user_response.userresponse_model_obj.filter(user_response = "No").count()

            # print(totalimgtested)
            # print(successfultests)
            # print(failedtests)
            return render(request,'adminHome.html',{'email':email,'name':name,'totalimgtested':totalimgtested,'successfultests':successfultests,'failedtests':failedtests})
        except:
            messages.error(request,'Wrong admin Info!!')
            return render(request,'AdminLogin.html')
    
    else:
        email=request.session['email']
        try:
            admins = adminuser.adminobject.get(email=email)
            name = admins.username
            totalimgtested = user_response.userresponse_model_obj.all().count()
            successfultests = user_response.userresponse_model_obj.filter(user_response = "Yes").count()
            failedtests = user_response.userresponse_model_obj.filter(user_response = "No").count()

            # print(totalimgtested)
            # print(successfultests)
            # print(failedtests)
            return render(request,'adminHome.html',{'email':email,'name':name,'totalimgtested':totalimgtested,'successfultests':successfultests,'failedtests':failedtests})
        except:
            messages.error(request,'Wrong admin Info!!')
            return render(request,'AdminLogin.html')


def adminprofile(request):
    email=request.session['email']
    try:
        userdetails=adminuser.adminobject.get(email=email)
        usname=userdetails.username
        upassword=userdetails.password
        uphone=userdetails.phone
        return render(request,"admin_profile.html",{'email': email,'name':usname,'password':upassword,'phone':uphone})
    except:
        messages.error(request,'Failed to get data from database!!')
        return render(request,'adminHome.html')


def updateadmin(request):
    if request.method=="POST":
        try:
           print(request.POST['email'])
           print()
           adminuser.adminobject.filter(email=request.POST['email']).update(username=request.POST['name'],password=request.POST['password'])
           messages.success(request, 'Your profile was updated successfully.')
           #Now to get new contents which are updated from database
           userdetails=adminuser.adminobject.get(email=request.POST['email'])
           usname=userdetails.username
           upassword=userdetails.password
           uphone=userdetails.phone
           return render(request,"admin_profile.html",{'email': request.POST['email'],'name':usname,'password':upassword})
  
        except:
            messages.error(request,'Failed to update profile')
            #Now to get new contents which are updated from database
            userdetails=adminuser.adminobject.get(email=request.POST['email'])
            usname=userdetails.username
            upassword=userdetails.password
            uphone=userdetails.phone
            return render(request,"admin_profile.html",{'email': request.POST['email'],'name':usname,'password':upassword,'phone':uphone})
    else:
        print("Method is not POST")

def userstable(request):
    #Fetching all users data from database 
    email=request.session['email']
    admins = adminuser.adminobject.get(email=email)
    name = admins.username  
    try:
        data =  Users.person.all()  
        return render(request,'usersTable.html',{'users':data,'email':email,'name':name})
    except:
        messages.error(request,'Error while opening your page!!')
        totalimgtested = user_response.userresponse_model_obj.all().count()
        successfultests = user_response.userresponse_model_obj.filter(user_response = "Yes").count()
        failedtests = user_response.userresponse_model_obj.filter(user_response = "No").count()

            # print(totalimgtested)
            # print(successfultests)
            # print(failedtests)
        return render(request,'adminHome.html',{'email':email,'name':name,'totalimgtested':totalimgtested,'successfultests':successfultests,'failedtests':failedtests})


def contactus_table_admin(request):
    #Fetching all users data from database 
    email=request.session['email']
    admins = adminuser.adminobject.get(email=email)
    try:
        data =  ContactusDB.contactdbobject.all()  
        name = admins.username  
        return render(request,'contactUsMessages.html',{'data':data,'email':email,'name':name})
    except:
        messages.error(request,'Error while opening your page!!')
        totalimgtested = user_response.userresponse_model_obj.all().count()
        successfultests = user_response.userresponse_model_obj.filter(user_response = "Yes").count()
        failedtests = user_response.userresponse_model_obj.filter(user_response = "No").count()

            # print(totalimgtested)
            # print(successfultests)
            # print(failedtests)
        return render(request,'adminHome.html',{'email':email,'name':name,'totalimgtested':totalimgtested,'successfultests':successfultests,'failedtests':failedtests})


def userReview(request):
    if request.method == "POST":
        #Getting values from form in variables
        try:
            imgpath = request.POST['filepath']
            email = request.session['Email']
            date = datetime.date.today()
            userresponse = request.POST['response']
            predicted = request.POST['result']

            #Now checking that variables are getting values from form
            # print(imgpath)
            # print(email)
            # print(date)
            # print(userresponse)
            # print(predicted)

            #Before rendering template firstly sending data to database model
            post = user_response()
            post.user_Email = email
            post.user_response = userresponse
            post.prediction_made = predicted
            post.image_path = imgpath
            post.date = date
            post.save()
            messages.success(request, 'Your review was successfully submitted.')
        except:
            messages.error(request,'Error while submitting your responser')     
        return render(request,'userDashboad.html')



def imagesuploadedAndTested(request):
    #Firstly accessing data from database
    try:
        uploadimgdata = user_response.userresponse_model_obj.all()
        return render(request,'imagesuploadedAndTested.html',{'uploadimgdata':uploadimgdata})
    except:
        messages.error(request,"Failed to Fetch Data from database")
        return render(request,'imagesuploadedAndTested.html')
