from django.db import models
from django.urls import reverse #Used to generate URLs by reversing the URL patterns
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from datetime import date


# Create your models here.
class Apart(models.Model):
    """
    Model representing an appartment
    """
    nbr = models.IntegerField(primary_key=True)
    descr = models.CharField(max_length=200)
    owner = models.ForeignKey('Owner', on_delete=models.SET_NULL, null=True)
    # Foreign Key used
    # appartment can only have one owner, but owner can have appartments
    # Owner as a string rather than object it hasn't been declared yet in the file
    sqr = models.IntegerField()
    summary = models.TextField(max_length=1000, help_text="Enter a appartment info")
    layout = models.ImageField(upload_to='apart')
    
    def __str__(self):
        """
        String for representing the Model object
        """
        return self.descr


    def get_absolute_url(self):
        """
        Returns the url to access a particular appartment instance
        """
        return reverse('apart-detail', args=[str(self.nbr)])

    class Meta:
        ordering = ['nbr']




class Owner(models.Model):
    """
    Model representing an owner
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    phone = PhoneNumberField(null=False, blank=False, unique=True)

    def get_absolute_url(self):
        """
        Returns the url to access a particular owner instance
        """
        return reverse('owner-detail', args=[str(self.id)])


    def __str__(self):
        """
        String for representing the Model object
        """
        return '%s, %s' % (self.last_name, self.first_name)

    class Meta:
        ordering = ['last_name']



class Service(models.Model):
    """
    Model representing an maintenance
    """
    prof = (('e','electric'), ('s','sanitary'), ('c','cleaning'))
    prof_req = models.CharField(max_length=1, choices=prof, 
        blank=True, default='s', help_text='Required service type')
    date_req = models.DateField(null=True, blank=True)    
    # client = models.ForeignKey('Apart', on_delete=models.SET_NULL, null=True, blank=True)
    client = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def is_busy(self):
        for date in date_req:
            if date:
                return True
        return False

    # def get_absolute_url(self):
    #     """
    #     Returns the url to access a particular owner instance
    #     """
    #     return reverse('service-list')

    def __str__(self):
        """
        String for representing the Model object
        """
        return '%s (%s)' % (self.client, self.prof_req, self.date_req)



class Accrual(models.Model):
    """
    Model representing an accruals
    """
    # nbr = models.ForeignKey('Apart', to_field = 'nbr', on_delete=models.SET_NULL, null=True, blank=True)   
    nbr = models.ForeignKey(User,  on_delete=models.SET_NULL, null=True, blank=True)
    accrued = models.IntegerField(null=True, blank=True)
    contrib = models.IntegerField(null=True, blank=True)
    confirm = models.BooleanField(null=True, default=False)
    balance = models.IntegerField(null=True, blank=True)
    
    

    def __str__(self):
        """
        String for representing the Model object
        """
        return '%s, %s' % (self.nbr, self.balance)


