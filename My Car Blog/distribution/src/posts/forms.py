from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
	
	
	class Meta:
		model = Post
		fields = ('title','overview','content','thumbnail','categories','featured','previous_post','next_post')

class CommentForm(forms.ModelForm):
	content = forms.CharField(widget=forms.Textarea(attrs={
		'class': 'form-control',
		'name': 'Type your name',
		'id':'usercomment',
		'placeholder': 'Type your comment',
		
		'rows':'4',
	}))
	
	class Meta:
		model = Comment
		fields = ('content',)
