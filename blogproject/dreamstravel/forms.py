from django import forms
from .models import Comments

class CommentsForm (forms.ModelForm):
    comments_email = forms.EmailField(required=True, label= 'Email', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your e-mail here'}))
    comments_lines = forms.CharField(required=True, label= 'Comment', widget=forms.Textarea(attrs={'rows':"3",'class': 'form-control', 'placeholder': 'Please enter your comment here'}))
    class Meta:
        model = Comments
        fields = ['comments_email', 'comments_lines']



