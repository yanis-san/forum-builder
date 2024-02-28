from django import forms
from pythonbb.models import Forum, Thread, Message

class CreateForumForm(forms.ModelForm):
    class Meta:
        model = Forum
        fields = ['title',
                  'description'
                  ]


class CreateThreadForm(forms.ModelForm):

    class Meta:
        model = Thread
        fields = ['title']
     
class CreateMessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ['content']


