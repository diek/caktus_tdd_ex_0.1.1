from django import forms


class ClueForm(forms.Form):
    user_guess = forms.CharField(label='Your guess', max_length=60)
