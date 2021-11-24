from django.shortcuts import render, redirect
from .forms import EmployeeForm,UserForm, PasswordForm
from .models import Employee, User
from django.contrib import messages
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def welcome(request):
    return render(request,'welcome.html')

def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request,'index.html',{'form':form})

def show(request):
    employees = Employee.objects.all()
    return render(request,"show.html",{'employees':employees})

def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request,'edit.html', {'employee':employee})

def update(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance = employee)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'employee': employee})

def destroy(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect("/show")

def register(request):
    user=User()
    if request.method == "POST":
        form= UserForm(request.POST, instance = user)
        password = request.POST["password"]
        repassword = request.POST["repassword"]
        if form.is_valid():
            if password == repassword:
                form.save()
                return redirect('/login')
            else:
                messages.success(request,'password and repasword dont match.Please re-enter')
                return render(request, 'messages.html')
    else:
        form = UserForm()
    return render(request, 'register.html', {'form': form})            

def login(request):
    if request.method == "POST":
        try:
           userdetails = User.objects.get(uemail=request.POST['uemail'],password=request.POST['password'])
           print("Email=", userdetails)
           request.session['Email']=userdetails.uemail
           return redirect('/show')
        except User.DoesNotExist:
            messages.success(request,'Invalid Entries....!')
            return render(request, 'messages.html') 
    return render(request,'login.html')
      
def send_mail(request):
    if request.method=="POST":
        try: 
            user =User.objects.get(uemail=request.POST['uemail'])
            print("Email=", user)
            request.session['Email']=user.uemail
            nemail=request.POST.get('uemail')
            mid=user.id 
            msg = MIMEMultipart()
            message = "Follow the link below inorder to recover your password\n" + "http://127.0.0.1:8000/entercode/" + str(mid)
            password = "password of the email below"
            msg['From'] = "put you source email here"
            msg['To'] = nemail
            msg['Subject'] = "Password Recovery link"

            msg.attach(MIMEText(message, 'plain'))
            server = smtplib.SMTP('smtp.gmail.com: 587')
            server.starttls()
            server.login(msg['From'], password)
            server.sendmail(msg['From'], msg['To'], msg.as_string())
            server.quit()
            return render(request, "password_reset_done.html" )
        except User.DoesNotExist: 
            messages.success(request,'Invalid Entries....!')
            return render(request, 'messages.html')                                         
    return render(request, 'reset_password.html')
    
def enter_code(request, id):
    user = User.objects.get(id=id)
    return render(request,'enter_code.html', {'user':user})

def enter_pass(request, id):
    user = User.objects.get(id=id)
    form = PasswordForm(request.POST, instance = user)
    if form.is_valid():
        form.save()
        return redirect("/login")
    return render(request, 'entercode', {'user': user})