from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField
# Create your models here.
class bridal(models.Model):


    type = models.CharField(max_length=150)
    sub_title = models.CharField(max_length=150)
    design = models.CharField(max_length=150)
    purpose = models.CharField(max_length=150)
    aouther_name = models.CharField(max_length=150)
    description = RichTextField()
    photo = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo1 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo2 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo3 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo4 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo5 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo6 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo7 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo8 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo9 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo10 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo11 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    cost = models.IntegerField()
    service_place = models.CharField(max_length=150)
    serial_no = models.IntegerField()
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.sub_title