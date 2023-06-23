from django import forms
import os 
import importlib
# importlib.import_module("...price-estimator.")
# from ...price-estimatr.
neighborhoods = []

class DataForm(forms.Form):
    location = forms.ChoiceField(required=True, choices=neighborhoods)
    rooms = forms.IntegerField(min_value=0, required=True)
    parking = forms.BooleanField()
    warehouse = forms.BooleanField()
    elevator = forms.BooleanField()

    def process_data(self, location, rooms, parking, warehouse, elevator):



        return "1245 toman per square meter"