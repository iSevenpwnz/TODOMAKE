from django import forms
from .models import Task, Tag


class TaskForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': 'What needs to be done?',
            'rows': 3
        }),
        help_text='Describe your task here'
    )

    deadline = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(attrs={
            'type': 'datetime-local'
        }),
        help_text='Leave empty if there\'s no specific deadline'
    )

    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        required=False,
        help_text='Hold Ctrl (Cmd on Mac) to select multiple tags'
    )

    class Meta:
        model = Task
        fields = ["content", "deadline", "tags"]


class TagForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter tag name (e.g., work, home, shopping)'
        }),
        help_text='Choose a short, descriptive name for your tag'
    )

    class Meta:
        model = Tag
        fields = ["name"]
