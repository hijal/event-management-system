from django import forms

class ForWhomForm(forms.Form):
    select = forms.CharField(
        widget = forms.RadioSelect
    )

class EventTypeForm(forms.Form):
    name = forms.CharField(
        widget = forms.RadioSelect(
            attrs={
                'class': 'form-control',
            }
        )
    )

class GuestNumberForm(forms.Form):
    number = forms.CharField(
        widget = forms.RadioSelect(
            attrs={
                'class': 'form-control',
            }
        )
    )

class DateInputForm(forms.Form):
    date = forms.CharField(max_length=120, widget = forms.TextInput())