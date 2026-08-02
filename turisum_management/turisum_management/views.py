from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def hotel_index(request):
    return render(request,'hotel_index.html')

def home(request):
    return render(request,'index.html')