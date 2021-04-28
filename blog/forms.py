from django import forms
from .models import Comment
from users.models import Profile

class SearchForm(forms.Form):
    query = forms.CharField()

class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
