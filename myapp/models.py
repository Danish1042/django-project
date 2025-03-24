from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Chaiverity(models.Model):
    CHAI_TYPE_CHOICE = [
        ('ML', 'MASALA'),
        ('GR', 'GINGER'),
        ('KL', 'KIWI'),
        ('PL', 'PLAIN'),
        ('EL', 'ELACHI'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/')
    date = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE)
    description = models.TextField(default='')
    price = models.TextField(default='')
    price = models.PositiveSmallIntegerField(default='')

    def __str__(self):
        return self.name
    
# One to Many
class ChaiReview(models.Model):
    chai = models.ForeignKey(Chaiverity, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username}, review for {self.chai.name}'
    
# Many to Many 
class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    chai_varities = models.ManyToManyField(Chaiverity, related_name='stores')

    def __str__(self):
        return self.name
    
# One to One
class ChaiCertificate(models.Model):
    chai = models.OneToOneField(Chaiverity, on_delete=models.CASCADE, related_name='certificate')
    certificate_number = models.CharField(max_length=100)
    issue_date = models.DateTimeField(default=timezone.now)
    valid_untill = models.DateTimeField()

    def __str__(self):
        return f'Certificate for {self.chai.name}'