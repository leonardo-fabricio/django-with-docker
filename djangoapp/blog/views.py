from django.shortcuts import render

# Create your views here.

def MyFunction(request):
    return render('blog/index.html')