from django import forms
from django.contrib.auth.forms import UserChangeForm
from .models import Blog

class BlogUpdate(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title','body']
# form 이용시 views.py 수정

# from .models import AttendHistroy
# class AttendHistroyFrom(forms.ModelForm):
#     class Meta:
#         model = AttendHistroy
#         fields = '__all__'