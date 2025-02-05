from django.db import models
import random

from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.conf import settings
from django.utils import timezone
from django.db import models
from django.forms import ModelForm
from django.core.exceptions import ValidationError


class Emploi(models.Model):
    """A model of a job."""
    JOB_TYPES = [("Sur site", "Sur site"), ("En ligne", "En ligne")]
    JOB_TYPES2 = [("Temps plein", "Temps plein"), ("Temps partiel", "Temps partiel")]
    JOB_DURATION = [("Temporaire","Temporaire"), ("Permanent","Permanent")]
    job_title = models.CharField(max_length=200, verbose_name="Titre du poste", null=True)
    entreprise_name = models.CharField(max_length=200, verbose_name="Nom de l'entreprise", null=True)
    entreprise_location = models.CharField(max_length=50, verbose_name="Localisation", null=True)
    reference = models.CharField(max_length=20, verbose_name="Reference", default="Ayd2023")
    job_duration = models.CharField(max_length=10, choices = JOB_TYPES, verbose_name="Contrat", default="Temporaire")
    job_type2 = models.CharField(max_length=15, choices = JOB_TYPES2, verbose_name="Horaire", default="Temps plein")
    job_type = models.CharField(max_length=10, choices = JOB_DURATION, verbose_name="Type d'emploi", default="Sur site")
    description = models.TextField(max_length=500, verbose_name="Description", null=True, blank=True)
    responsabilities = models.TextField(max_length=500, verbose_name="Responsabilités", null=True, blank=True)
    qualifications = models.TextField(max_length=500, verbose_name="Qualifications", null=True, blank=True)
    deadline = models.DateField(verbose_name="Dernier délai", null=True)
    close = models.BooleanField(default=False, verbose_name="Dossier fermé", null=True)
    published_date = models.DateTimeField(auto_now_add=True, verbose_name="Date de publication", null=True)

    def func_reference(self):
        ref3 = self.entreprise_name
        ref2 = ''.join(list(map(lambda x: x.strip(), ref3.split())))
        ref = ref2[0:4].upper() + str(random.randint(1, 9999))    
        return ref
    
    def save(self, *args, **kwargs) :
        self.reference = self.func_reference()
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.job_title}" 
'''  
class Message(models.Model):
    """A model of a message."""
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=16)
    content = models.CharField(max_length=500)
    sent_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.name}"
'''