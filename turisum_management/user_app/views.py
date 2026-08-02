from django.shortcuts import render,redirect
from .models import*
from admin_app.models import Package_details,hotel_adbooking_details
# Create your views here.
def register(request):
    if request.method=="POST":
       username=request.POST.get('username')
       useremail=request.POST.get('useremail')
       userpassword=request.POST.get('userpassword')
       userphone=request.POST.get('userphone')
       usercity=request.POST.get('usercity')

       data=user_register(username=username,useremail=useremail,
                        userpassword=userpassword,userphone=userphone,
                        usercity=usercity,)
       data.save()
     
       return render(request,'register.html')
    
    return render(request,'register.html')


def login(request):

     if request.method=="POST":
        useremail=request.POST.get('useremail')
        userpassword=request.POST.get('userpassword')

        # admin
        if useremail=='admin@gmail.com' and userpassword=='admin':
            request.session['useremail']=useremail
            request.session['admin']='admin'
            return render(request,'index.html',{'status':'Admin login successfull'})   
        # user     
        elif user_register.objects.filter(useremail=useremail,userpassword=userpassword).exists():
            user_exp=user_register.objects.get(useremail=request.POST['useremail'],userpassword=userpassword)

            if user_exp.userpassword==request.POST['userpassword']:
                request.session ['uid']=user_exp.id
                request.session ['uname']=user_exp.username
                request.session ['uemail']=user_exp.useremail
                request.session ['user']='user'
                return render(request,'index.html',{'status':'Your  login successfull...'}) 
           
        else:
            return render(request,'login.html',{"status": "Login Failed"})
     return render(request,'login.html')


def logout(request):
    session_keys=list(request.session.keys())
    for key in session_keys:
        del request.session[key]
        return redirect(login)


# ...package..
def view_packages(request):
    pk_data=Package_details.objects.all()
    return render(request,'view_packages.html',{'result':pk_data})




def booking(request):
    pk_data = Package_details.objects.all()
    if request.method == "POST":

        user_name = request.POST.get('user_name')
        user_email = request.POST.get('user_email')
       
        user_phone = request.POST.get('user_phone')
        user_destination = request.POST.get('user_destination')

        data = booking_app(
            user_name=user_name, user_email=user_email,
             user_phone=user_phone,
            user_destination=user_destination,)

        data.save()

        return redirect("/")

    return render(request,'booking.html',{'pk_data': pk_data } )


def contact_us(request):
    if request.method=="POST":
       username_c=request.POST.get('username_c')
       useremail_c=request.POST.get('useremail_c')
       userphone_c=request.POST.get('userphone_c')
       message_c=request.POST.get('message_c')

       data=contact_us_details(username_c=username_c,useremail_c=useremail_c,userphone_c=userphone_c, message_c=message_c,)
       data.save()
     
       return render(request,'contact_us.html')
    return render(request,'contact_us.html')


def user_booking_view(request):
    data_hb=hotel_adbooking_details.objects.all()
    return render(request,'user_booking_view.html',{'result':data_hb})


