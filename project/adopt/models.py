from django.db import models

from django.utils.translation import gettext as _

class Pet(models.Model):
    name = models.CharField(
            help_text=_('Names of animal'),
            max_length = 100,
    )

    species = models.CharField(
            help_text=_('Species of animal'),
            max_length = 50,
    )


    birth_date = models.DateField(
            help_text = _('birth_date'),
    )
    
    MALE = 'male'
    FEMALE = 'female'
    OTHER = 'other'

    SEX_CHOICES = (
            (MALE,'Male'),
            (FEMALE, 'Female'),
            (OTHER, 'Other'),
    )


    sex = models.CharField(
            help_text = _('Sex of pet'),
            max_length = 16,
            choices = SEX_CHOICES,
            default = OTHER,
    )
    
    def __str__(self):
        return self.name





