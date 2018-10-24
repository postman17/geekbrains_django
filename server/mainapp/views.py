from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'mainapp/index.html')

def about(request):
    context = {'about': 'about'}
    return render(request, 'mainapp/about.html', context)

def contacts(request):
    return render(request, 'mainapp/contacts.html')