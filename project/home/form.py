from typing import Any
from django import forms
from .models import Post
from .models import Comment
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','body','image','status']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nhập Tên Bài Viết'}),
            'content': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Nhập Nội Dung'}),
        }

class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop('author', None)
        self.post = kwargs.pop('post', None)
        super ().__init__(*args, **kwargs)
    def save(self, commit = True):
        comment =  super().save(commit= False)
        comment.author = self.author
        comment.post = self.post
        comment.save()
    class Meta:
        model = Comment
        fields = ["body"]

class CommentDeleteForm(forms.Form):
    confirm_delete = forms.BooleanField(label='Xác nhận xóa', required=True)