from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views.decorators.http import require_GET, require_POST
from django.views import View
from app1.forms import TodoForm

# def index(request):
#     return HttpResponse("Hello")

apptodo = {
    1: ['Buy Milk', True],
    2: ['Pay bills', False],
    3: ['Test task', True ],
    }

def index(request):
    context = {
        'title':'Welcome to app1',
        'content':'Kjo eshte Homepage'
    }
    return render(request, 'homepage.html', context)


def view_apps(request, apps_id):
    if apps_id not in apptodo.keys():
        # return HttpResponse('Todo with id ' + '\"'+str(apps_id)+'\"' + ' doesn\'t exist!' )
        raise Http404('Todo with id ' + '\"'+str(apps_id)+'\"' + ' doesn\'t exist!')
    todo = apptodo[apps_id]
    context ={
        'todo': todo

    }
    return render(request, 'view-app.html', context)
    # return HttpResponse('Apps: ' + str(apps_id))

# def todo_form(request):
#     return render(request, 'create-todo.html')

# @require_POST
def create_todo(request):
    if request.method == "POST":
        # return HttpResponse(request.POST['todo'])
        new_todo=request.POST['todo']
        next_index=len(apptodo.keys()) + 1
        apptodo[next_index] = [new_todo, False] 
        return render (request, 'create-todo.html', {'apptodo':apptodo})        
    return render (request, 'create-todo.html')
   
   
    # id = apps_id
    # index = {
    #     'title':'View Page | Django',
    #     'content':'Ky eshte kontent',
    #     id:id
    # }
    # return render(request, 'view.html', index)

# class-base views
class TodoView(View):
    template_location = 'create-todo.html'
    
    def get(self, request):
        form = TodoForm
        context={

            'form':form
        }
        # return HttpResponse("I am GET route")
        return render(request,self.template_location, context)
    def post(self,request):
        # return HttpResponse('I am POST route')
        form = TodoForm(request.POST)
        if form.is_valid():
            new_todo=request.POST['todo']
            next_index=len(apptodo.keys()) + 1
            apptodo[next_index] = [new_todo, False]
            context = {

                'form':form,
                'apptodo':apptodo
            }
            return render (request, self.template_location, context)
        else:
            return render(request, self.template_location, {'form':form})