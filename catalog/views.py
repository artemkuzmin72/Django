from django.shortcuts import render

def home(request):
    return render(request,'home.html')


def contacts(request):
    return render(request,'contacts.html')


def example_view(request):
    return render(request,'catalog/example.html')