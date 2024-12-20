from django.db import models

# Create your models here.
# schema:Property
# fields:id,place,price,category,bedroom_count,squarefootage

class Property(models.Model):
    place = models.CharField(max_length=200)
    price = models.FloatField()
    
    CATEGORY_CHOICES = (
        ('house', 'House'),
        ('villas', 'Villas'),
        ('flat', 'Flat'),
    )
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    bedroom_count = models.IntegerField()
    square_footage = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)