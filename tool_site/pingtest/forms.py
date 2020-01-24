from django import forms

class PingForm(forms.Form):
    subnet = forms.CharField(max_length = 15, min_length = 7)
    start = forms.IntegerField(max_value = 255, min_value = 1)
    end = forms.IntegerField(max_value = 255, min_value = 1)
