from django.contrib import messages
from django.db import models
from datetime import datetime
from django.core.validators import RegexValidator
from phone_field import PhoneField

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bridal_id = models.IntegerField()
    customer_need = models.CharField(max_length=150)
    bridal_title = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=150)
    email = models.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = PhoneField(blank=True, help_text='Contact phone number')
    fax_number = PhoneField(blank=True)# validators should be a list
    messagees = models.TextField(max_length=500)
    user_id = models.IntegerField()
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.email