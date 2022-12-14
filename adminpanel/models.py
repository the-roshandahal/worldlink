from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Slider(models.Model):
    image = models.ImageField(upload_to='slider_images')
    main_text = models.CharField(max_length=200)
    second_text = models.CharField(max_length=200)
    third_text = models.CharField(max_length=200)
    custom_url = models.URLField(null=True, blank=True)
    order = models.PositiveIntegerField(default="1")

    def __str__(self):
        return self.main_text
    class Meta:
        verbose_name_plural = "  Slider" 

class TourCategory(models.Model):
    category = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default="1")
    is_active = models.BooleanField(default=1)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.category
    class Meta:
        verbose_name_plural = " TourCategory" 


class Destination(models.Model):
    location = models.CharField(max_length=400)
    image = models.ImageField(upload_to='destination_images')
    created = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.location

class Tour(models.Model):
    tour_name = models.CharField(max_length=10000000)
    tour_category = models.ForeignKey(TourCategory, on_delete=models.CASCADE)
    tour_location = models.ForeignKey(Destination, on_delete=models.CASCADE, null=True,blank=True)
    time = models.CharField(max_length=10000000)
    availability = models.CharField(max_length=10000000)
    min_age = models.CharField(max_length=10000000)
    max_people = models.CharField(max_length=10000000)
    tour_details = models.CharField(max_length=10000000)
    itinerary = models.CharField(max_length=10000000)
    price = models.CharField(max_length=10000000)
    offered_price =models.CharField(max_length=10000000, null=True,blank=True)
    featured_image= models.ImageField(upload_to="tour_image")
    image1 = models.ImageField(upload_to="tour_image", null=True,blank=True)
    image2 = models.ImageField(upload_to="tour_image", null=True,blank=True)
    image3 = models.ImageField(upload_to="tour_image", null=True,blank=True)
    created = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.tour_name
    

class Blog(models.Model):
    title = models.CharField(max_length=1000)
    blog = models.TextField()
    image = models.ImageField(upload_to="blogs_images/")
    created = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title

class Testimonial(models.Model):
    testimonial= models.CharField(max_length=5000)
    name= models.CharField(max_length=5000)
    
    star= models.PositiveIntegerField(
          validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )
    image=models.ImageField(upload_to='testimonial_images')
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Partner(models.Model):
    name = models.CharField(max_length=400)
    logo = models.ImageField(upload_to='partner_images')
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=400)
    position = models.CharField(max_length=400)
    image = models.ImageField(upload_to='team_images')
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=1000)
    email = models.CharField(max_length=1000)
    subject = models.CharField(max_length=1000)
    contact = models.CharField(max_length=1000)
    message = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class Booking(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    no_of_travellers = models.CharField(max_length=100)
    def __str__(self):
        return self.name



class CompanySetup(models.Model):
    data_set = models.CharField(max_length=100)
    header_logo = models.ImageField(upload_to="company_images")
    footer_logo = models.ImageField(upload_to="company_images")
    location = models.CharField(max_length=1000)
    primary_contact = models.CharField(max_length=1000)
    secondary_contact = models.CharField(max_length=1000)
    primary_email = models.CharField(max_length=1000)
    secondary_email = models.CharField(max_length=1000)
    opening_hours = models.CharField(max_length=100)
    years_of_experience = models.CharField(max_length=100)
    tour_packages = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    happy_customers = models.CharField(max_length=100)
    facebook_url = models.URLField()
    instagram_url = models.URLField()
    twitter_url = models.URLField()

    def __str__(self):
        return self.data_set