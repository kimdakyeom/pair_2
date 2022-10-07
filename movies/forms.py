from django.forms import ModelForm, TextInput, NumberInput
from .models import Review


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
        widgets = {
            'title' : TextInput(attrs={
                'class':'form-control',
                'placeholder':'Title',
            }),
            'content' : TextInput(attrs={
                'class':'form-control ',
                'placeholder':'content',
                'style' : 'height:300px;'
            }),
            'movie_name' : TextInput(attrs={
                'class':'form-control',
                'placeholder':'movie_name)'
            }),
        }
        