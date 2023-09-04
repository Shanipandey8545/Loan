from django.shortcuts import render,redirect
from .models import Contactus,Applynow,Homeloan,Personalloan,Buisnessloan,User_Reg
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method=='GET':
        return render(request, 'loanapp/html/index.html')
    
def aboutus(request):
    if request.method=='GET':
        return render(request, 'loanapp/html/aboutus.html')
    
    
def blog(request):
    if request.method=='GET':
        return render(request, 'loanapp/html/blog.html')    
    
    
def contactus(request):
    if request.method=='GET':
        return render(request, 'loanapp/html/contactus.html') 
    if request.method=='POST':
        name=request.POST["name"]
        phone=request.POST["phone"] 

        email=request.POST["email"] 
        message=request.POST["message"] 
        contact=Contactus(name=name,phone=phone,email=email,message=message)
        contact.save()
        print("save data")
        return render(request, 'loanapp/html/contactus.html') 

        
          
    
def loan(request):
    if request.method=='GET':
        return render(request, 'loanapp/html/loan.html')            
    
def applynow(request):
    if request.method=='GET':
        return render(request, 'loanapp/html/applynow.html')    
    
    if request.method=="POST":
        fname=request.POST["firstname"]
        lname=request.POST["lastname"]
        pincode=request.POST["pincode"]
        mnumber=request.POST["mobilenumber"]
        
        aplnow=Applynow(firstname=fname,lastname=lname,pincode=pincode,mobilenumber=mnumber)
        aplnow.save()
        print("save data")
        return render(request, 'loanapp/html/applynow.html')    
    
    
    
    

def homeloan(request):
    if request.method=='GET':
        return render(request, 'loanapp/html/homeloan.html')            
    
    if request.method=='POST':
        mnumber=request.POST["mobilenumber"]
        loantype=request.POST["loantype"]
        amount=request.POST["amount"]
        property=request.POST["property"]
        
        homeloan=Homeloan(mobilenumber=mnumber,loantype=loantype,amount=amount,property=property)
        homeloan.save()
        print("save data")
        return render(request, 'loanapp/html/homeloan.html') 
    
    
    
               

def personalloan(request):
    if request.method=='GET':
        return render(request, 'loanapp/html/personalloan.html') 
    if request.method=='POST':
        mnumber=request.POST["mobilenumber"]
        emptype=request.POST["employeetype"]
        
        ploane=Personalloan(mobilenumber=mnumber,employeetype=emptype)
        ploane.save()
        print("save data")
        return render(request, 'loanapp/html/personalloan.html') 
    
    
    

def buisnessloan(request):
    if request.method=='GET':
        return render(request, 'loanapp/html/buisnessloan.html')            
    if request.method=='POST':
        name=request.POST["name"]
        city=request.POST["city"]
        amount=request.POST["amount"]
        employed=request.POST["employed"]
        turnover=request.POST["turnover"]
        mobilenumber=request.POST["mobilenumber"]
       
        buisnessloan=Buisnessloan(name=name,city=city,amount=amount,employed=employed,turnover=turnover,mobilenumber=mobilenumber)
        buisnessloan.save()
        print("save data")
        return render(request, 'loanapp/html/buisnessloan.html') 
    
    
               
def user_home(request):
    if request.method=='GET':
        user_id=request.session["session_key"]

        user_object=User_Reg.objects.get(u_id=user_id)
        context={                           
                "user_data":user_object  
            }
        return render(request, 'loanapp/html/user_home.html',context)  
    
def user_login(request):
    if request.method=='GET':
        return render(request, 'loanapp/html/user_login.html')  
    if request.method=='POST':
        user_id=request.POST["id"]  
        user_password=request.POST["password"]
        list=User_Reg.objects.filter(u_id=user_id,password=user_password)
        l=len(list)
        if l>0:
            request.session["session_key"]=user_id 
            request.session["role"]="user" 
            user_object=User_Reg.objects.get(u_id=user_id)
            context={                           
                "user_data":user_object  
            }
            return render(request, 'loanapp/html/user_home.html',context)  
        else:
            messages.error(request, "Invalid User_id or Password")  

            return render(request, 'loanapp/html/user_login.html')  



    
def user_reg(request):
    if request.method=='GET':
        return render(request, 'loanapp/html/user_reg.html')   
    if request.method=='POST':
        user_id=request.POST["userid"] 
        user_password=request.POST["password"]
        user_name=request.POST["name"]
        user_email=request.POST["email"]
        user_phone=request.POST["phone"]
        user_city=request.POST["city"]
        user_gender=request.POST["gender"]
        user_address=request.POST["address"]  
        user=User_Reg(u_id=user_id,password=user_password,name=user_name,email=user_email,phone=user_phone,city=user_city,gender=user_gender,address=user_address)
        user.save()
        print("save data")
        messages.success(request, "Dear User Thanks For Registration")  
        
        return render(request, 'loanapp/html/user_reg.html')   
        

def logout(request):
    del request.session["session_key"]
    del request.session["role"]
    return redirect("/")
                  
    