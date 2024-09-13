from django import forms
from .models import Comment
from .models import Post
from taggit.forms import TagWidget

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']  # Add 'tags' here
        widgets = {
            'tags': TagWidget(),
        }