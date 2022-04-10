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


class QueryData(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    email = models.EmailField(unique=True,null=True,blank=True,error_messages={'unique':'This email already exists!'})
    ph_no = models.BigIntegerField(null=True,blank=True)
    message = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add = True)
    
    class Meta:
        db_table = 'query_data'
    
    def __str__(self):
        return self.name + ' ' + self.email
    