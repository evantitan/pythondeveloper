from django import forms
from .models import Comment, Bookmark, Review


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
        widgets = {
          'body': forms.Textarea(attrs={'rows':2, 'cols':2}),
          'name': forms.Textarea(attrs={'rows':1, 'cols':2}),
          'email': forms.Textarea(attrs={'rows':1, 'cols':2})
        }

class UserCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        widgets = {
          'body': forms.Textarea(attrs={'rows':2, 'cols':40}),
        }
        labels = {
            'body': "add your comment"
        }

class SearchForm(forms.Form):
    query = forms.CharField()

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('name', 'email', 'suggestion', 'rating')
