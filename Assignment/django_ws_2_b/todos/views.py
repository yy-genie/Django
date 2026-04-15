from django.shortcuts import render

todos = []
# Create your views here.
def index(request):
    work = request.GET.get("work")
    todos.append(work)
    context = {
        "todos" : todos
    }
    return render(request, 'todos/index.html', context)

def create_todo(request):
    return render(request, 'todos/create_todo.html')