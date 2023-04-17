from django.db import models

# Create your models here.
class Covid(models.Model):
    Country=models.CharField(max_length=255)
    Total_Confirmed_Cases=models.CharField(max_length=255)
    Total_Deaths_Cases=models.CharField(max_length=255)
    Total_Recovered_Cases=models.CharField(max_length=255)
    Date=models.DateField(auto_now_add=False) 
    

    def __str__(self):
     return self.Country