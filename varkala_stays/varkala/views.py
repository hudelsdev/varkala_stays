from django.shortcuts import render

# Create your views here.
def varkala_index(request):
    return render(request, "varkala/index.html")
