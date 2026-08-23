from django import forms


class DebugForm(forms.Form):
    checkbox = forms.BooleanField(help_text="Help text.")
