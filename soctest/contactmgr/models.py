from django.db import models

# Create your models here.

class ContactList(models.Model):
    name	= models.CharField(max_length=20)
    address1	= models.CharField(max_length=255)
    city	= models.CharField(max_length=50)
    state	= models.CharField(max_length=2)
    postal_code	= models.CharField(max_length=10)
    country	= models.CharField(max_length=10)
    phone_number= models.CharField(max_length=13)

    @classmethod
    def get_contacts(cls):
        return ContactList.objects.all().order_by('pk')
