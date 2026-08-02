"""
URL configuration for turisum_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('add_package',views.add_package, name="add_package"),
    path('ad_package_view',views.ad_package_view,name= "ad_package_view"),
    path('package_del/<int:id>',views.package_del,name="package_del"),
    path('update_packages/<int:id>',views.update_packages, name="update_packages"),
    path('update_packages/update_packages_data/<int:id>',views.update_packages_data, name="update_packages_data"),
    path('booking_view',views.booking_view,name='booking_view'),
    path('approve_booking/<int:id>',views.approve_booking,  name='approve_booking'),
    path('reject_booking/<int:id>',views.reject_booking, name='reject_booking'),
    path('contact_us_view',views.contact_us_view,name="contact_us_view"),
    path('hotel_booking',views.hotel_booking, name="hotel_booking"),
    path('ad_hbooking_view/',views.ad_hbooking_view,name='ad_hbooking_view'),
    path('booking_delete/<int:id>/', views.booking_delete, name='booking_delete')



    
    

    
]
