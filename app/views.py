from django.shortcuts import redirect, render
#Importing logout for logout function
from django.contrib.auth import logout
from app.models import Users,ContactusDB
from django.contrib import messages

#For uploading files to server we need
from django.core.files.storage import FileSystemStorage

# Create your views here.
def home(request):
    #Before calling home ending any use session using logout(request) function this won't through any error
    #if no user has loggin
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
        

def AdminSignin(request):

    return render(request,'AdminLogin.html')

def userDashboard(request):
    if request.method=="POST":
        try:
            userdetails=Users.person.get(umail=request.POST['umail'],upassword=request.POST['upassword'])
            request.session['Email']=userdetails.umail
            email=request.POST['umail']
            #Requesting session so that we can use it to access it in user profile
            usname=userdetails.username
            return render(request,"userDashboad.html",{'email': email,'name':usname})
        except:
            messages.error(request,'Failed to login No Such User exits')
            return render(request,'LoginAndSignUp.html')
    else:
        email=request.session['Email']
        return render(request,"userDashboad.html",{'email': email})

    


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





    if(classes == 0):
        print("Combination")
    elif(classes==1):
        print("Emblem")  
    elif(classes==2):
        print("Lettermark")
    elif(classes==3):
        print("Wordmark")

    return render(request,'userDashboad.html',{'filepathname':filepathname})