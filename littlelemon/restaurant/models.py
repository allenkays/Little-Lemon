from django.db import models

# Create your models here.
class Booking(models.Model):
    Name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField(default=6)
    BookingDate= models.DateField()
    

class Menu(models.Model):
    Title = models.CharField(max_length=255)
    Price = models.IntegerField(null=False)
    Inventory = models.SmallIntegerField(default=10)
    
    def __str__(self):
        return f'{self.title}: {self.price}'
    