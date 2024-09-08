from django.shortcuts import render, redirect
from datetime import date
from .models import Task
from .form import NewTaskForm
from django.db.models import Q
# Create your views here.

def home(request):
    Task.objects.create(title="Task 1", status="To Do",due_date=date.today())
    tasks = Task.objects.all().order_by('due_date','priority')
    priority = [0, 'High', 'Medium', 'Low']
    for i in tasks:
        print(i.due_date)
        print(i.priority,type(i.priority),priority[i.priority])
        print(i.title)
    return render(request, 'home.html', {'tasks': tasks,'priority':priority})

def add_task(request):
    if request.method == 'POST':
        form = NewTaskForm(request.POST)
        if form.is_valid():
            form.save()
            my_date = form.cleaned_data.get('my_date_field')
            if my_date is not None and date.today is not None:

             if my_date <= date.today:
                form.add_error('my_date_field', 'Please enter a future date.')
                return render(request, 'add_task.html', {'form': form})
            return redirect('home')
    else:
        form = NewTaskForm()
    return render(request, 'add_task.html', {'form': form})

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('home')

def edit_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        form = NewTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            my_date = form.cleaned_data.get('my_date_field')
            if my_date is not None and date.today is not None:
             if my_date <= date.today():
                form.add_error('my_date_field', 'Please enter a future date.')
                return render(request, 'edit_task.html', {'form': form, 'task': task})
            return redirect('home')
    else:
        form = NewTaskForm(instance=task)
    return render(request, 'edit_task.html', {'form': form, 'task': task})


def detail_task(request, task_id):
    task = Task.objects.get(id=task_id)
    priority=[0,'High','Medium','Low']
    print(priority[task.priority])
    print(task.priority)
    return render(request, 'detail.html', {'task': task,'priority':priority})


def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        tasks = Task.objects.filter(title__contains=searched)
        return render(request, 'search.html', {'searched': searched, 'tasks': tasks})
    else:
        return render(request, 'search.html')

def item(request):
    query= request.GET.get('query','')
    status=['To Do','In Progress','Done']
    category_id=request.GET.get('category',0)
    print(category_id)
    if category_id and query=='':

        items = Task.objects.filter(status=category_id)
        print(items,"fuck",Task.objects.all())
        for item in items:
            print(item.title)
        for item in Task.objects.all():
            print(item.title,item.status)
    elif category_id and query:
        items = Task.objects.filter(Q(title__icontains=query)|Q(description__icontains=query)|Q(due_date__icontains=query))
        items=items.filter(status=category_id)

    elif query:
         items=Task.objects.filter(Q(title__icontains=query)|Q(description__icontains=query)|Q(due_date__icontains=query))
    else:
     items=Task.objects.all()
    items=items.order_by('due_date','priority')


    return render(request,"items.html",{
        'items': items,
        'query': query,
        'categories':status,
        'category_id':category_id,
    })