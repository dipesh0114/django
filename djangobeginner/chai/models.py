from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Chaivariety(models.Model):
    CHAI_TYPE_CHOICES = [
        ('ML', 'MASALA'),   
        ('GR', 'GINGER'),   
        ('KL', 'KIWI'),   
        ('PL', 'PLAIN'),   
        ('EL', 'ELAICHI'),   
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/')
    data_added = models.DateTimeField(default=timezone.now)
    type= models.CharField(
        max_length=2,
        choices=CHAI_TYPE_CHOICES)
    description = models.TextField(default="")


    def __str__(self):
        return self.name
    
    # one to many

class ChaiReview(models.Model):
    chai = models.ForeignKey(Chaivariety, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    comment = models.TextField(default="")
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} - {self.chai.name} Review"
    

# many to many 

class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    chai_varieties = models.ManyToManyField(Chaivariety, related_name='stores')

    def __str__(self):
        return self.name
    
#one to one 

class ChaiCertificate(models.Model):
    chai = models.OneToOneField(Chaivariety, on_delete= models.CASCADE, related_name='Certificate')
    certificate_number = models.CharField(max_length=100)
    issued_date = models.DateTimeField(default=timezone.now)
    valid_until = models.DateTimeField()

    def __str__(self):
        return f' certificate for {self.chai.name}'
    
    