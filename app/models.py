from django.db import models
from django.db.models.base import Model

# Create your models here.
#Models are simply database tables, We can create multiple of them
class Users(models.Model):
    #Ceating columns in our table
    username=models.CharField(max_length=50)
    upassword=models.CharField(max_length=50)
    umail=models.EmailField(max_length=50)
    uphone=models.CharField(max_length=15)

    #Giving model manager name which we will use to access data base
    person=models.Manager()
    class Meta:
        #This will create table with above fields with name below users
        db_table="users"

class ContactusDB(models.Model):
    #Now for columns
    cname=models.CharField(max_length=50)
    csubject=models.CharField(max_length=100)
    cphonenumber=models.CharField(max_length=15)
    cemail=models.EmailField(max_length=50)
    cmsg=models.CharField(max_length=1000)

    contactdbobject=models.Manager()
    class Meta:
        db_table="ContactUStable"


class adminuser(models.Model):
    #Ceating columns in our table
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=10)
    email=models.EmailField(max_length=50)
    phone=models.CharField(max_length=15)

    #Giving model manager name which we will use to access data base
    adminobject=models.Manager()
    class Meta:
        #This will create table with above fields with name below users
        db_table="admin_user"

    
class user_response(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    #you use primary_key = True if you do not want to use default field "id" given by django to your model
    user_Email = models.EmailField(max_length=30)
    image_path = models.CharField(max_length=50)
    prediction_made = models.CharField(max_length=100)
    user_response = models.CharField(max_length=10)
    date = models.DateField(max_length=20)

    #Now defining object of our model
    userresponse_model_obj = models.Manager()
    class Meta:
        db_table = "user_result_response"
