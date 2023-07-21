from .models import *
from django.forms import ModelForm

class carform(ModelForm):

    class Meta:
        model = car
        fields  = ('marka','cost')