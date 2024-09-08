from django import forms
from .models import Task

Input_class='w-full py-4 px-6 rounded-xl border'
class NewTaskForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=('title','priority','status','due_date','description')
        widgets={

            'title':forms.TextInput(attrs={'class':Input_class}),
            'priority':forms.Select(attrs={'class':Input_class}),
            'status':forms.Select(attrs={'class':Input_class}),
            'due_date':forms.DateInput(attrs={'class':Input_class}),
            'description':forms.Textarea(attrs={'class':Input_class}),
        }