from django.db import models

# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length =100, blank= False, null= False)
    email= models.EmailField(blank=False)
    phone = models.CharField(max_length =10, blank= False, null= False)
    message = models.TextField(blank= False,null= False)

    def __str__(self):
        return self.name + ' ' + self.email

class Volunteer(models.Model):
    name = models.CharField(max_length=100, blank= False, null= False)
    email = models.EmailField(blank= False, null= False)
    city = models.CharField(max_length=100, blank= False)
    help = models.TextField(blank= False, null= True)

    def __str__(self):
        return self.name + ' ' + self.email


class Plant(models.Model):
    name = models.CharField(max_length =100)
    email = models.EmailField()
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name + ' ' + self.email

class Send(models.Model):
    fname = models.CharField(max_length=100, blank= False, null= False)
    lname = models.CharField(max_length=100, blank= False, null= False)
    email = models.EmailField(blank= False, null= False)
    message = models.TextField(max_length=100, blank= False)


    def __str__(self):
        return self.fname + ' ' + self.email
