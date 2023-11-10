from django import forms
from .models import TodoList, TodoItem

class TodoListForm(forms.ModelForm):
    class Meta():
        model = TodoList
        fields = ["title"]
        

class TodoItemForm(forms.ModelForm):
    class Meta():
        model = TodoItem
        fields = ["title", "description"]
    