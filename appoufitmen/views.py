from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')

def Casual(request):
    return render (request, "Casual.html")

def Formal(request):
    return render (request, "Formal.html")