from django import forms
from price_estimator.House_price_predictor import predict_price
from price_estimator.clean_df import result

neighborhoods = result

class DataForm(forms.Form):
    location = forms.ChoiceField(required=True, choices=neighborhoods)
    rooms = forms.IntegerField(min_value=0, required=True)
    parking = forms.BooleanField(required=False, initial=False)
    warehouse = forms.BooleanField(required=False, initial=False)
    elevator = forms.BooleanField(required=False, initial=False)

    def process_data(self, location, rooms, parking, warehouse, elevator):
        price = predict_price(rooms, int(parking), int(warehouse), int(elevator), float(location))
        answer = str(f"{int(round(price*1000000, -4 )):,}") 
        return answer
