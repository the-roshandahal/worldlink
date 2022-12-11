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

    def __str__(self):
        return self.category
    class Meta:
        verbose_name_plural = " TourCategory" 


class Destination(models.Model):
    location = models.CharField(max_length=400)
    image = models.ImageField(upload_to='destination_images')
    def __str__(self):
        return self.location

class Tour(models.Model):
    tour_name = models.CharField(max_length=10000000)
    tour_category = models.ForeignKey(TourCategory, on_delete=models.CASCADE)
    tour_location = models.ManyToManyField(Destination)

    time = models.CharField(max_length=10000000)
    availability = models.CharField(max_length=10000000)
    min_age = models.CharField(max_length=10000000)
    max_people = models.CharField(max_length=10000000)
    tour_details = models.CharField(max_length=10000000)
    itinerary = models.CharField(max_length=10000000)
    price = models.CharField(max_length=10000000)
    featured_image= models.ImageField(upload_to="tour_image")
    image1 = models.ImageField(upload_to="tour_image", null=True,blank=True)
    image2 = models.ImageField(upload_to="tour_image", null=True,blank=True)
    image3 = models.ImageField(upload_to="tour_image", null=True,blank=True)
    image4 = models.ImageField(upload_to="tour_image", null=True,blank=True)

    def __str__(self):
        return self.tour_name
    

class Blog(models.Model):
    title = models.CharField(max_length=1000)
    blog = models.TextField()
    image = models.ImageField(upload_to="blogs_images/")
    created = models.DateTimeField(auto_now_add=True, null=True)

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

    def __str__(self):
        return self.name
