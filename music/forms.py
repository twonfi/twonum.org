from django import forms
from music import models


class TrackAdderForm(forms.Form):
    release = forms.ModelChoiceField(queryset=models.Release.objects.all())
    text = forms.CharField(widget=forms.Textarea, help_text=r'Track number, space, title, newline. Example: "01 Prologue[n]02 First Steps".')
