from django.db import models

# Create your models here.
class Institutes_details(models.Model):
    institute_id = models.IntegerField()
    institute_name = models.CharField(max_length=60)
    institute_address = models.CharField(max_length=80)
    institute_slug = models.SlugField(unique=True)
    institute_image = models.ImageField(upload_to='images')
    institute_email = models.EmailField(unique=True)

    def __str__(self):
        return f'{self.institute_name}'


class Vaninfo(models.Model):
    van_id = models.IntegerField()
    driver_name = models.CharField(max_length=200)
    driver_con = models.CharField(max_length=11)
    van_no = models.CharField(max_length=10)
    total_seats = models.IntegerField()
    available_seats = models.IntegerField()
    destination = models.CharField(max_length=200)
    current = models.CharField(max_length=200)
    van_slug = models.SlugField(unique=True)
    van_image = models.ImageField(upload_to='images')
    Institutes_details = models.ForeignKey(Institutes_details, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.driver_name} - {self.van_no}'

