from django.http import HttpResponse
from django.shortcuts import render

from familiar.models import Familiar


def create_familiar(request):
    new_familiar = Familiar.objects.create(name='juan', apellido='alessi')
    print(new_familiar)
    return HttpResponse('Se creo el familiar')

def list_familiar(request):
    all_products = Familiar.objects.all()
    context = {
        'familiar':all_products,
    }
    return render(request, 'familiar/list_familiar.html', context=context)
