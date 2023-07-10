from django.shortcuts import render

finches = [
    {'name': 'Alex', 'breed': 'House finch', 'description': 'friendly', 'age': 3},
    {'name': 'Nala', 'breed': 'Pine siskin', 'description': 'mean and grumpy', 'age': 8},
    {'name': 'Sidney', 'breed': 'Purple finch', 'description': 'shy', 'age': 4}
]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', {
        'finches': finches
    })