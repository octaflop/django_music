from django import forms


class SongForm(forms.Form):
    track = forms.IntegerField(label='Track', required=False)
    title = forms.CharField(label='Title')
    duration = forms.CharField(label='Duration', max_length=15, required=False)
