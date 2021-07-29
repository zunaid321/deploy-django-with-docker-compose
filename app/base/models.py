from django.db import models

# Create your models here.

def upload_service_image(instance,filename):
    return "service/{filename}".format(filename = filename)

def upload_news_image(instance,filename):
    return "news/{filename}".format(filename = filename)

def upload_client_image(instance,filename):
    return "clients/{filename}".format(filename = filename)

class Service(models.Model):
    SERVICE_CHOICES = [
        ('CBT', 'Cross Border Transactions'),
        ('CC', 'Corporate & Compliance'),
        ('CRE', 'Construction & Real Estate'),
        ('CT', 'Commercial Transactions'),
        ('DR', 'Dispute Resolution'),
        ('EL', 'Employment & Labor'),
    ]
    type = models.CharField(max_length=3, choices=SERVICE_CHOICES, default= 'CBT')
    heading = models.CharField(max_length=50, default='')
    image = models.ImageField(upload_to=upload_service_image, null =True, blank=True)
    content = models.TextField(default='')
    
    def __str__(self) -> str:
        return self.heading

class News(models.Model):
    heading = models.CharField(max_length=50, default='')
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to=upload_news_image, null =True, blank=True)
    content = models.TextField(default='')

    class Meta:
        verbose_name_plural = "News"

    def __str__(self) -> str:
        return self.heading

class Client(models.Model):
    name = models.CharField(max_length=50, default='')
    logo = models.ImageField(upload_to=upload_client_image, null =True)

    def __str__(self) -> str:
        return self.name

class Contact(models.Model):
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')
    email = models.CharField(max_length=50, default='')
    message = models.TextField(default='')
    address = models.CharField(max_length=150, default='')

    def __str__(self) -> str:
        return self.email


