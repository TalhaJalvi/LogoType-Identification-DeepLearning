from django.db import models

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
    ausername=models.CharField(max_length=50)
    apassword=models.CharField(max_length=10)
    amail=models.EmailField(max_length=50)
    aphone=models.CharField(max_length=15)

    #Giving model manager name which we will use to access data base
    adminobject=models.Manager()
    class Meta:
        #This will create table with above fields with name below users
        db_table="admin_user"