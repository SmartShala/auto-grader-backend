from django.db import models

# Create your models here.
class Testimonial(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    testimonial = models.TextField(null=True,blank=True)
    designation = models.CharField(max_length=100,null=True,blank=True)
    image = models.ImageField(upload_to='testimonial_images/',null=True,blank=True)
    
    class Meta:
        db_table = 'testimonial_data'
        
    def __str__(self):
        return self.name