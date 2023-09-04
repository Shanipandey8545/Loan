from django.db import models
from django.utils import timezone


# Create your models here
 
 
 
 
class Contactus(models.Model):
    name=models.CharField(max_length=50,null=False)
    phone=models.CharField(max_length=50,null=False)
    email=models.EmailField(max_length=50,null=False)
    message=models.CharField(max_length=50,null=False)
    date=models.DateField(default=timezone.now)
    
    def __str__(self):
        return self.email
  
Gender=[
   ( "M","MALE"),
    ("F","FEMALE")
 ]
class User_Reg(models.Model):
    u_id=models.CharField(max_length=45,null=False, primary_key=True)
    password=models.CharField(max_length=45,null=False)
    name=models.CharField(max_length=45,null=False)
    email=models.EmailField(max_length=45,null=False)
    phone=models.CharField(max_length=10,null=False)
    city=models.CharField(max_length=45,null=False)
    gender=models.CharField(max_length=6,choices=Gender,null=False)
    address=models.TextField()
    date=models.DateField(default=timezone.now)
    
    def __str__(self):
        return self.name  
    
    
class Applynow(models.Model):
    firstname=models.CharField(max_length=50,null=False)
    lastname=models.CharField(max_length=50,null=False)
    pincode=models.IntegerField(max_length=50,null=False)
    mobilenumber=models.IntegerField(max_length=50,null=False)
    def __str__(self):
        return self.firstname
  
LOANTYPE=[
      ("newhome","newhome"),
      ("balancetransfer","balancetransfer")
  ]
  
    
class Homeloan(models.Model):
    mobilenumber=models.IntegerField(max_length=50,null=False)
    loantype=models.CharField(max_length=50,choices=LOANTYPE, null=False)
    amount=models.CharField(max_length=50,null=False)
    property=models.CharField(max_length=50,null=False)
    apply_date=models.DateField(default=timezone.now)
    
    def __str__(self):
        return self.loantype
    
    
employeetype=[
        ("salaried","salaried"),
      ("selfsalaried","selfsalaried")
  ]
        
     
class Personalloan(models.Model):
    mobilenumber=models.IntegerField(max_length=50,null=False) 
    employeetype=models.CharField(max_length=50, choices=employeetype, null=False)
    apply_date=models.DateField(default=timezone.now)
       
    def __str__(self):
        return self.apply_date
               
               
               
class Buisnessloan(models.Model):
    name=models.CharField(max_length=50,null=False)
    city=models.CharField(max_length=50,null=False)
    amount=models.IntegerField(max_length=50,null=False) 
    employed=models.CharField(max_length=50,null=False)
    turnover=models.CharField(max_length=50,null=False)
    mobilenumber=models.IntegerField(max_length=10,null=False)
    apply_date=models.DateField(default=timezone.now)
    
    def __str__(self):
        return self.name
     
     

                