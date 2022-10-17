from django import forms

class TodoForm(forms.Form):
    todo = forms.CharField(label='Enter Todo: ', max_length=20)
