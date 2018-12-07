from django.db import models
from django.contrib.auth.models import User
#from django.core.validations import 

# Create your models here.
class UserProfile(models.Model):
    create_at = models.DateField(auto_now= True)
    street = models.CharField(max_length=45)
    city = models.CharField(max_length=45)
    colony = models.CharField(max_length=45)
    state = models.CharField(max_length=45)
    country = models.CharField(max_length=45)
    zip_code = models.IntegerField()
    phone = models.CharField(max_length=45)
    user = models.OneToOneField(User, on_delete= models.CASCADE, primary_key= True)

class Vaccine(models.Model):
    name = models.CharField(max_length=45, null= False)
    description = models.TextField(null = False)



class Antiparasitic(models.Model):
    name = models.CharField(max_length=45, null= False)
    description = models.TextField(null = False)

class Animal(models.Model): 
    name = models.CharField(max_length=200, null= False)
    chip =  models.IntegerField()
    adoption_day = models.DateField(null= False)
    species = models.CharField(max_length=45, null= False)
    breed = models.CharField(max_length=45)
    color = models.CharField(max_length=45)
    sex = models.CharField(max_length=45)
    castrating = models.BooleanField(null= False)
    pedigree = models.CharField(max_length=45)
    tattoo = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    dead = models.BooleanField(null= True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class ClinicalRecord(models.Model):
    examination_date = models.DateField()
    diagnostic = models.TextField()
    treatment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    vaccines = models.ManyToManyField(Vaccine, through='Inmunization')
    antiparasitic = models.ManyToManyField(Antiparasitic, through='Deworming')

class Inmunization(models.Model):
    clinical_record = models.ForeignKey(ClinicalRecord, on_delete=models.CASCADE)
    vaccine = models.ForeignKey(Vaccine, on_delete=models.CASCADE)
    batch = models.IntegerField()
    application_date = models.DateField()
    reapplication_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

class Deworming(models.Model):
    clinical_record = models.ForeignKey(ClinicalRecord, on_delete=models.CASCADE)
    antiparasitic = models.ForeignKey(Antiparasitic, on_delete=models.CASCADE)
    application_date = models.DateField(null = False)
    reapplication_date = models.DateField(null = False)
    created_at = models.DateTimeField(auto_now_add=True)

class UserVet(models.Model):
    cedula_profesional = models.IntegerField()
    clinic_name = models.CharField(max_length = 45)
    user = models.OneToOneField(User, on_delete= models.CASCADE, primary_key= True)

    def __str__(self):
        return 'UserVet: {}'.format(self.user.username)
    
    #animal = models.ManyToManyField(Animal, through='Animal', related_name='animal')
    #members = models.ManyToManyField (Person, through= 'Memebership')

