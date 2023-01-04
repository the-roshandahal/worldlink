from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Slider(models.Model):
    order = models.TextField()
    image = models.ImageField(upload_to='slider_images')
    text_1 = models.TextField(null=True,blank=True)
    text_2 = models.TextField(null=True,blank=True)
    text_3 = models.TextField(null=True,blank=True)
    text_4 = models.TextField(null=True,blank=True)
    custom_link = models.URLField(null=True,blank=True)

    def __str__(self):
        return self.text_1
    class Meta:
        verbose_name_plural = " Slider" 

class TourCategory(models.Model):
    category = models.TextField()
    order = models.PositiveIntegerField(default="1")
    is_active = models.BooleanField(default=1)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.category
    class Meta:
        verbose_name_plural = " TourCategory" 


class Destination(models.Model):
    location = models.TextField()
    image = models.ImageField(upload_to='destination_images')
    created = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.location

class Tour(models.Model):
    tour_name = models.TextField()
    tour_category = models.ForeignKey(TourCategory, on_delete=models.CASCADE)
    tour_location = models.ForeignKey(Destination, on_delete=models.CASCADE, null=True,blank=True)
    drop_location =models.TextField(null=True,blank=True)
    time = models.TextField()
    availability = models.TextField()
    min_age = models.TextField()
    max_people = models.TextField()
    tour_details = models.TextField()
    itinerary = models.TextField()
    price = models.TextField()
    featured_image= models.ImageField(upload_to="tour_image")
    image1 = models.ImageField(upload_to="tour_image", null=True,blank=True)
    image2 = models.ImageField(upload_to="tour_image", null=True,blank=True)
    image3 = models.ImageField(upload_to="tour_image", null=True,blank=True)
    is_featured = models.BooleanField(null=True)
    created = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.tour_name
    class Meta:
        verbose_name_plural = "    Tours & Trekking" 
    

class Blog(models.Model):
    title = models.TextField()
    blog = models.TextField()
    image = models.ImageField(upload_to="blogs_images/")
    created = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title

class Testimonial(models.Model):
    testimonial= models.TextField()
    name= models.TextField()
    
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
    name = models.TextField()
    logo = models.ImageField(upload_to='partner_images')
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.TextField()
    position = models.TextField()
    image = models.ImageField(upload_to='team_images')
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.TextField()
    email = models.TextField()
    subject = models.TextField()
    contact = models.TextField()
    message = models.TextField()

    def __str__(self):
        return self.name

class Booking(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    name = models.TextField()
    email = models.TextField()
    contact = models.TextField()
    no_of_travellers = models.TextField()
    def __str__(self):
        return self.name



class CompanySetup(models.Model):
    data_set = models.TextField()

    header_logo = models.ImageField(upload_to="company_images")
    footer_logo = models.ImageField(upload_to="company_images")
    
    location = models.TextField()
    primary_contact = models.TextField()
    secondary_contact = models.TextField()
    primary_email = models.TextField()
    secondary_email = models.TextField()
    opening_hours = models.TextField()

    years_of_experience = models.TextField()
    tour_packages = models.TextField()
    happy_customers = models.TextField()
    destination = models.TextField()
    
    facebook_url = models.URLField()
    instagram_url = models.URLField()
    twitter_url = models.URLField()

    about_us_page_heading_text = models.TextField()
    about_us_page_content = models.TextField()

    def __str__(self):
        return self.data_set
