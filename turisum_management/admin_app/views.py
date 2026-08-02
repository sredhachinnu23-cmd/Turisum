from django.shortcuts import render,redirect
from .models import*
from user_app.models import booking_app,contact_us_details


# Create your views here.
def add_package(request):
     if request.method=="POST":
       image=request.FILES.get('image')
       packagename=request.POST.get('packagename')
       package=request.POST.get('package')
       location=request.POST.get('location')
       days=request.POST.get('days')

       data=Package_details(image=image,packagename=packagename,
                        package=package,location=location,
                        days=days,)
       data.save()
     
       return render(request,'add_package.html')
     return render(request,'add_package.html')

def ad_package_view(request):
    pk_data=Package_details.objects.all()
    return render(request,'ad_package_view.html',{'result':pk_data})

def package_del(request,id):
    pk_data=Package_details.objects.get(pk=id)
    pk_data.delete()
    return redirect(ad_package_view)

def update_packages(request,id):
    pk_data=Package_details.objects.get(pk=id)
    return render(request,'update_packages.html',{'result':pk_data})

def update_packages_data(request,id):
    if request.method=="POST":
       image=request.FILES.get('image')
       packagename=request.POST.get('packagename')
       package=request.POST.get('package')
       location=request.POST.get('location')
       days=request.POST.get('days')
       data=Package_details(id=id, image=image,packagename=packagename,
                            package=package,location=location,
                            days=days,)
       data.save()
       return redirect(ad_package_view)
    return render(request,'update_packages.html')


def booking_view(reequest):
    bk_data=booking_app.objects.all()
    return render(reequest,'booking_view.html',{'result':bk_data})


def approve_booking(request,id):
    data = booking_app.objects.get(id=id)
    data.status = "Approved"
    data.save()
    return redirect('booking_view')


def reject_booking(request,id):
    data = booking_app.objects.get(id=id)
    data.status = "Rejected"
    data.save()
    return redirect('booking_view')


def contact_us_view(request):
    data_c=contact_us_details.objects.all()
    return render(request,'contact_us_view.html',{'result':data_c})

def hotel_booking(request):
    if request.method=="POST":
      username_hb=request.POST.get('username_hb')
      useremail_hb=request.POST.get('useremail_hb')
      userphone_hb=request.POST.get('userphone_hb')
      hotel_name=request.POST.get('hotel_name')
      check_in=request.POST.get('check_in')
      check_out=request.POST.get('check_out')
      guest=request.POST.get('guest')
      vehicle_hb=request.POST.get('vehicle_hb')
      destination=request.POST.get('destination')
      data=hotel_adbooking_details( username_hb=username_hb,useremail_hb=useremail_hb,
                            hotel_name=hotel_name,check_in=check_in,
                            check_out=check_out,guest=guest,vehicle_hb=vehicle_hb,userphone_hb=userphone_hb,destination=destination,)
      data.save()
      return render(request,'hotel_booking.html')

    return render(request,'hotel_booking.html')

def ad_hbooking_view(request):
    data_1=hotel_adbooking_details.objects.all()

    return render (request,'ad_hbooking_view.html',{'result':data_1})


def booking_delete(request,id):
    data_2 = hotel_adbooking_details.objects.get(pk=id)
    data_2.delete()
    return redirect('ad_hbooking_view')