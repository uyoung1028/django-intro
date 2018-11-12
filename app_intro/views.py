from django.shortcuts import render
import random

# Create your views here.
def index(request):
    return render(request, 'index.html')

def lunch(request):
    menu_list = ['20층', '김카', '시골집']
    pick = random.choice(menu_list)
    return render(request, 'lunch.html', {'pick': pick})

def lotto(request):
    num_list = list(range(1,46))
    pick = random.sample(num_list, 6)
    return render(request, 'lotto.html', {'pick': sorted(pick)})
    
def hello(request, name):
    return render(request, 'hello.html', {'name': name})
    
def cube(request, num):
    return render(request, 'cube.html', {'num': num**3})