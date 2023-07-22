from django.forms import ModelForm
from .models import Occupancy 

class OccupancyForm(ModelForm):
    class Meta:
        model=Occupancy
        fields='__all__'