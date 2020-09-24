from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import Http404
from django.http import HttpResponse
from .forms import MedicineForm
from .models import *

# Create your views here.
class DashboardIndexView(View):
    def get(self, request):
        medicines = Medicine.objects.all()
        context = {
            'medicines' : medicines
        }
        return render(request, 'dashboard.html', context)
    
    def post(self, request):
        return render(request, 'medReg.html')

class RegistrationView(View):
    def get(self, request):
       # print('get')
        return render(request, 'medReg.html')
    
    def post(self, request):
        form = MedicineForm(request.POST)
        if form.is_valid():
            category1 = request.POST.get("category")
            genericName1 = request.POST.get("genericName")
            commonBrand1 = request.POST.get("commonBrand")
            manufacturedDate1 = request.POST.get("manufacturedDate")
            expiryDate1 = request.POST.get("expiryDate")
            size1 = request.POST.get("size")
            howToUse1 = request.POST.get("howToUse")
            sideEffects1 = request.POST.get("sideEffects")
            price1 = request.POST.get("price")
            noOfItems1 = request.POST.get("noOfItems")
            
            form = Medicine(category = category1, genericName = genericName1, commonBrand = commonBrand1, manufacturedDate = manufacturedDate1, expiryDate = expiryDate1, size = size1,
                    howToUse = howToUse1, sideEffects = sideEffects1, price = price1, noOfItems = noOfItems1)
           
            form.save()
            return HttpResponse("Successful")
        else:
            print(form.errors)
            return HttpResponse("failed")

    
            


