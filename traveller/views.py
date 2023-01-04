from django.shortcuts import render,redirect
from .models import *
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    slider = Slider.objects.all().order_by("order")
    
    destination = Destination.objects.all()
    paginator = Paginator(destination, 4)
    page = request.GET.get("page")
    destination = paginator.get_page(page)

    tour = Tour.objects.filter(is_featured = '1')
    paginator = Paginator(tour, 3)
    page = request.GET.get("page")
    tour = paginator.get_page(page)

    category = TourCategory.objects.all()
    blog = Blog.objects.all()
    testimonial = Testimonial.objects.all()
    partner = Partner.objects.all()

    if CompanySetup.objects.filter()[:1].exists():
        company = CompanySetup.objects.filter()[:1].get()
        context = {
            'slider':slider,
            'company':company,
            'destination':destination,
            'tour':tour,
            'category':category,
            'blog':blog,
            'testimonial':testimonial,
            'partner':partner
        }
    else:
        context = {
            'destination':destination,
            'tour':tour,
            'category':category,
            'blog':blog,
            'testimonial':testimonial,
            'partner':partner
        }
    return render(request,'index.html',context)


def destinations(request):
    company = CompanySetup.objects.filter()[:1].get()
    destination = Destination.objects.all()

    context = {
        'company':company,
        'destination':destination,
    }

    return render(request,'destinations.html',context)

def tours(request):
    company = CompanySetup.objects.filter()[:1].get()
    tours = Tour.objects.all()

    paginator = Paginator(tours, 9)
    page = request.GET.get("page")
    tours = paginator.get_page(page)

    partner = Partner.objects.all()
    context = {
        'partner':partner,
        'company':company,
        'tours':tours,
    }
    return render(request,'tours.html',context)
    
    
def tour_single(request,id):
    company = CompanySetup.objects.filter()[:1].get()
    tour = Tour.objects.get(id=id)
    context = {
        'company':company,
        'tour':tour,

    }
    return render(request,'tour_single.html',context)


def about_us(request):
    company = CompanySetup.objects.filter()[:1].get()

    testimonial = Testimonial.objects.all()
    team = Team.objects.all()
    partner = Partner.objects.all()
    context = {
        'company':company,
        'team':team,
        'testimonial':testimonial,
        'partner':partner
    }
    return render(request,'about_us.html',context)


def blogs(request):
    company = CompanySetup.objects.filter()[:1].get()
    blogs = Blog.objects.all()
    context = {
        'company':company,
        'blogs':blogs,
    }
    return render(request,'blogs.html',context)

    
def contact_us(request):
    company = CompanySetup.objects.filter()[:1].get()
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        contact = request.POST["contact"]
        message = request.POST["message"]
        Contact.objects.create(
            name=name, email=email, subject=subject, contact=contact, message=message
        )
        return redirect('home')
    else:
        return render(request,'contact_us.html',{'company':company})




def blog_single(request,id):
    company = CompanySetup.objects.filter()[:1].get()
    blog = Blog.objects.get(id=id)
    partner = Partner.objects.all()
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 2)
    page = request.GET.get("page")
    blogs = paginator.get_page(page)
    context = {
        'company':company,
        'blog':blog,
        'blogs':blogs,
        'partner':partner
    }
    return render(request,'blog_single.html',context)

def book_trip(request,id):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        contact = request.POST["contact"]
        no_of_travellers = request.POST["no_of_travellers"]
        tour = Tour.objects.get(id=id)
        Booking.objects.create(
            tour=tour, name=name, email=email, contact=contact, no_of_travellers=no_of_travellers
        )
        return redirect('tours')
    else:
        return redirect('tours')



def destination_filter(request,id):
    company = CompanySetup.objects.filter()[:1].get()

    tours = Tour.objects.filter(tour_location_id = id)

    partner = Partner.objects.all()
    context = {
        'company':company,
        'partner':partner,
        'tours':tours,
    }
    return render(request,'tours.html',context)
