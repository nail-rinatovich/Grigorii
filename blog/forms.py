# forms.py
from django import forms
from .models import game, Image

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image',)

class PostForm(forms.ModelForm):
    class Meta:
        model = game
        fields = ('title', )

PostImageFormSet = forms.inlineformset_factory(game, Image, form=ImageForm, extra=1)
