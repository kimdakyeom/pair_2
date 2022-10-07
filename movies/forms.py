from django.forms import ModelForm, TextInput, NumberInput
from .models import Review


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
        labels = {'title': '제목', 'content': '내용', 'movie_name': '영화 제목', 'grade': '별점', 'genre': '장르'}
        widgets = {
            'title' : TextInput(attrs={
                'class':'form-control',
                'placeholder':'글 제목',
            }),
            'content' : TextInput(attrs={
                'class':'form-control ',
                'placeholder':'내용',
                'style' : 'height:300px;'
            }),
            'movie_name' : TextInput(attrs={
                'class':'form-control',
                'placeholder':'영화 제목'
            }),
        }
        