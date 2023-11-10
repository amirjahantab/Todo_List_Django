from django.shortcuts import render
from .models import TodoList, TodoItem
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import TodoListForm, TodoItemForm
from django.shortcuts import redirect
# from django.http import JsonResponse

# Create your views here.
@login_required
def lists(request):
    form = TodoListForm()
    user = request.user
    lists = TodoList.objects.filter(user=user)
    
    if request.method == "POST":
        form = TodoListForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            new_list = TodoList(title=title, user=user)
            new_list.save()
            form = TodoListForm()
            
    return render(request, "todoapp/list.html", {'lists':lists, 'form':form})
            
            

@login_required
def list_detail(request, id):
    select_list = TodoList.objects.get(id=id)
    items = select_list.items
    form = TodoItemForm()

    if request.method == "POST":
        form = TodoItemForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            new_item = TodoItem(title=title, description=description, todo_list=select_list)
            new_item.save()

            # Create a new instance of the form
            form = TodoItemForm()

            context = {
                "select_list": select_list,
                "items": items,
                "form": form,
            }
            return render(request, "todoapp/detail.html", context)

    context = {
        "select_list": select_list,
        "items": items,
        "form": form,
    }
    return render(request, "todoapp/detail.html", context)

    

def delete_list(request, id):
    select_list = TodoList.objects.get(id=id)
    if request.method == "POST":
        select_list.delete()
        return redirect("lists")
    