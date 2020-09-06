from django import forms
from .models import Jasoseol, Comment

class JssForm(forms.ModelForm):
    class Meta:
        model = Jasoseol
        fields = ('title', 'content',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)

