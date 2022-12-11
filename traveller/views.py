from django.shortcuts import render
from adminpanel.models import *

# Create your views here.
def home(request):
    slider = Slider.objects.all().order_by('order')
   
    destination = Destination.objects.all()
    tour = Tour.objects.all()
    category = TourCategory.objects.all()
    blog = Blog.objects.all()
    testimonial = Testimonial.objects.all()
    context = {
        'slider':slider,
        'destination':destination,
        'tour':tour,
        'category':category,
        'blog':blog,
        'testimonial':testimonial
    }
    return render(request,'index.html',context)


def destinations(request):
    destinations = Destination.objects.all()
    context = {
        'destinations':destinations,

    }
    return render(request,'destinations.html',context)

def tours(request):
    tours = Tour.objects.all()
    
    context = {
        'tours':tours,

    }
    return render(request,'tours.html',context)
    
def tour_single(request,id):
    return render(request,'tour_single.html')