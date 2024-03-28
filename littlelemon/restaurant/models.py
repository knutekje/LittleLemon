from django.db import models

# Create your models here.
class Menu(models.Model):
    title = models.CharField(max_length=250, db_index=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, db_index=True)
    inventory = models.SmallIntegerField()


class Booking (models.Model):
    Name = models.CharField(max_length=250, db_index=True)
    no_of_guests = models.SmallIntegerField()
    bookingdate = models.DateField()
    