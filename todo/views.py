from django.shortcuts import render, redirect
from todo.models import Todo

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    return render(request, 'todo/index.html', {'todos': todos})
    
def new(request):
    return render(request, 'todo/new.html')
    
def create(request):
    title = request.POST.get('title')
    deadline = request.POST.get('deadline')
    todo = Todo(title=title, deadline=deadline)
    todo.save()
    return redirect('/todos/')

def read(request, id):
    todo = Todo.objects.get(id=id)
    return render(request, 'todo/read.html', {'todo': todo})
    
def todo_create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        deadline = request.POST.get('deadline')
        Todo.objects.create(title=title, deadline=deadline)
        return redirect('/todos/')
    else:
        return render(request, 'todo/todo_create.html')
        
def update(request, id):
    todo = Todo.objects.get(id=id)
    if request.method == "POST":  # 저장로직
        todo.title = request.POST.get('title')
        todo.deadline = request.POST.get('deadline')
        todo.save()
        return redirect('/todos/')
        
    else:  # 폼 보여주기
        deadline = todo.deadline.strftime("%Y-%m-%d")
        return render(request, 'todo/update.html', {'todo': todo, 'deadline': deadline})
        
def delete(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('/todos/')