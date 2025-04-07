from django import forms

FOLDS = ((5,5),(8,8),(10,10))
EPOCHS = ((100,100),(500,500),(1000,1000))

CRIME_RATE = ((0,"0%"),(10,"10%"), (20,"20%"),(30,"30%"))
PARKING_AREA = ((11, "1 Bike"),(12, "2 Bikes"),(13, "3 bikes"),(14, "4 Bike"),(15, "5 Bikes"),(16, "6 bikes"), (17, "7 Bikes"),(18, "8 bikes"),
                (21, "1 Car"),(22, "2 Cars"),(23, "3 Cars"),(24, "4 Car"),(25, "5 Cars"),(26, "6 Cars"), (27, "7 Cars"),(28, "8 Cars"),
                (31, "1 Car & 1 Bike"),(32, "1 Car & 2 Bike"),(33, "2 Car & 1 Bike"),(34, "2 Car & 2 Bike"))
HOUSE_TOWARDS = ((2, "Sun Side"),(1, "Back Side"),(0, "None"))
SUPPLY_OF_WATER = ((7,"Daily"),(6, "Good"),(5, "Average"), (4, "After a day"),(3, "After two days"),(2, "After three days"), (1, "After a week"), (0, "None"))
QUALITY_OF_GAS = ((4, "Good"),(3, "Medium"),(2, "Normal"), (1, "Poor"))
PROPERTY_TYPE = ((3, "Commercial"),(2, "Residential"),(1, "None"))
HOUSE_NEARBY = ((4, "Main Road"),(3, "Main Street"),(2, "Street"),(1, "None"))
HOUSE_TYPE = ((4, "RCC"),(3, "PAKKA"),(2, "Kacha"),(1, "None"))


class InputForm(forms.Form): 
    crime_rate = forms.CharField(widget=forms.Select(choices=CRIME_RATE))
    crime_rate.widget.attrs.update({'id':'input_crime_rate', 'class':'form-control'})
    parking_area = forms.CharField(widget=forms.Select(choices=PARKING_AREA))
    parking_area.widget.attrs.update({'id':'input_parking_area', 'class':'form-control'})
    house_towards = forms.CharField(widget=forms.Select(choices=HOUSE_TOWARDS))
    house_towards.widget.attrs.update({'id':'input_house_towards', 'class':'form-control'})
    supply_of_water = forms.CharField(widget=forms.Select(choices=SUPPLY_OF_WATER))
    supply_of_water.widget.attrs.update({'id':'input_supply_of_water', 'class':'form-control'})
    quality_of_gas = forms.CharField(widget=forms.Select(choices=QUALITY_OF_GAS))
    quality_of_gas.widget.attrs.update({'id':'input_quality_of_gas', 'class':'form-control'})
    property_type = forms.CharField(widget=forms.Select(choices=PROPERTY_TYPE))
    property_type.widget.attrs.update({'id':'input_property_type', 'class':'form-control'})
    house_near_by = forms.CharField(widget=forms.Select(choices=HOUSE_NEARBY))
    house_near_by.widget.attrs.update({'id':'input_house_near_by', 'class':'form-control'})
    house_type = forms.CharField(widget=forms.Select(choices=HOUSE_TYPE))
    house_type.widget.attrs.update({'id':'input_house_type', 'class':'form-control'})
    stories = forms.CharField()
    stories.widget.attrs.update({'id':'input_stories', 'class':'form-control'})
    bathrooms = forms.CharField()
    bathrooms.widget.attrs.update({'id':'input_bathrooms', 'class':'form-control'})
    kitchens = forms.CharField()
    kitchens.widget.attrs.update({'id':'input_kitchens', 'class':'form-control'})
    rooms = forms.CharField()
    rooms.widget.attrs.update({'id':'input_rooms', 'class':'form-control'})
    address = forms.CharField()
    address.widget.attrs.update({'id':'input_address', 'class':'form-control'})
    land_area = forms.CharField()
    land_area.widget.attrs.update({'id':'input_land_area', 'class':'form-control'})

    
    