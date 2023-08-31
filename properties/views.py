from django.shortcuts import render, redirect
from .models import property
from .forms import propertyForm

# Create your views here.
#logic to handle what happens when user goes to a page on website

# CRUD - Create, retrieve, update, delete, list

def property_list(request):
    properties = property.objects.all()
    
    #context - data to be passed
    context = {
        "properties": properties
    }
    return render(request, "properties.html", context)
 
def property_retrieve(request, pk):
    properties = property.objects.get(id=pk)
    context = {
         "properties": properties
    }
    return render(request, "property.html", context)

def property_create(request):
    form = propertyForm()
    if request.method == "POST":
        form = propertyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        
        
    context = {
        "form": form
    }
    return render(request, "property_create.html", context)

def property_update(request, pk):
    properties = property.objects.get(id=pk)
    form = propertyForm(instance=properties)
    if request.method == "POST":
        form = propertyForm(request.POST, instance=properties )
        if form.is_valid():
            form.save()
            return redirect("/")
        
        
    context = {
        "form": form
    }
    return render(request, "property_update.html", context)

def property_delete(request, pk):
    properties = property.objects.get(id=pk)
    properties.delete()
    return redirect("/")
        
        