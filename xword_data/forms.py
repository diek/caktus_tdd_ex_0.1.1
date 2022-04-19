from django import forms


class ClueForm(forms.Form):
    answer = forms.CharField(label='Your guess', max_length=60)
