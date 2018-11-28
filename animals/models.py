from django.db import models

# Create your models here.

class Animal(models.Model): 
    name = models.CharField(max_length=200, null= False)
    chip =  models.IntegerField
    adoption_day = models.DateField(null= False)
    species = models.CharField(max_length=45, null= False)
    breed = models.CharField(max_length=45)
    color = models.CharField(max_length=45)
    sex = models.CharField(max_length=45)
    castrating = models.DateField
    pedigree = models.CharField(max_length=45)
    tattoo = models.CharField(max_length=45, unique= True)
    created_at = models.DateField(auto_now=True)
    modifed_at = models.DateTimeField(auto_now=True)

class Clinical_Record(models.Model):
    examinations = models.DateField
    diagnostic = models.CharField(max_length=45)
    treatment = models.CharField(max_length=45)
    created_at = models.DateField(auto_now=True)
    modifed_at = models.DateField(auto_now=True)

class Inmunization(models.Model):
    batch = models.IntegerField
    application_date = models.DateField
    reapplication_date = models.DateField
    due_date = models.DateField

class Vaccines(models.Model):
    name = models.CharField(max_length=45, null= False)
    description = models.TextField(null = False)

class Wormed(models.Model):
    application_date = models.DateField(null = False)
    reapplication_date = models.DateField(null = False)

class Worm(models.Model):
    name = models.CharField(max_length=45, null= False)
    description = models.TextField(null = False)

class User(models.Model):
    username = models.CharField(max_length=16, null = False)
    email = models.EmailField(null = False)
    password = models.CharField(max_length=45)
    create_at = models.DateField(auto_now= True)
    street = models.CharField(max_length=45)
    city = models.CharField(max_length=45)
    colony = models.CharField(max_length=45)
    state = models.CharField(max_length=45)
    country = models.CharField(max_length=45)
    zip_code = models.IntegerField
    phone = models.CharField(max_length=45)

class Uservet(models.Model):
    licensed = models.IntegerField


    #members = models.ManyToManyField (Person, through= 'Memebership')

