from django.db import models

class ContactsList(models.Model):
    name = models.CharField(max_length=80, blank=False)
    last_name = models.CharField(max_length=80, verbose_name='last name', blank=True)
    phone_number = models.BigIntegerField(verbose_name='phone number', null=False)
    address = models.CharField(max_length=180, blank=True)


    def __str__(self) -> str:
        return f'{self.name}: {self.phone_number}'
        

