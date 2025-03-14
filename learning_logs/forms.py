from django import forms
from . models import Topic, Entry
# create a class that inherits from forms.ModelForn
class TopicForm(forms.ModelForm):
    # nested class tells django which model to base the form on and which fields to include
    class Meta:
        model = Topic
        # only include a text field
        fields = ['text']
        # do not generate a label for text field
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text' : 'Entry'}
        widgets = {'text' : forms.Textarea(attrs={'cols':80})}
