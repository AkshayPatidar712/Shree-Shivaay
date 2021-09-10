from django.shortcuts import render, HttpResponse
# from .models import Pesticide, Insecticide, Herbicide
from .models import *


def index(request):
    return render(request, 'index.html')


def product(request):
    return render(request, 'product.html')


def pesticide(request):
    return render(request, 'pesticide.html', )


def insecticide(request):
    insect = Insecticide.objects.all()
    return render(request, 'insecticide.html', {'insect': insect})


def herbicide(request):
    herbi = Herbicide.objects.all()
    return render(request, 'herbicide.html', {'herbi': herbi})


def fungicide(request):
    fungi = Fungicide.objects.all()
    return render(request, 'fungicide.html', {'fungi': fungi})


def fertilizer(request):
    ferti = Fertilizer.objects.all()
    return render(request, 'fertilizer.html', {'ferti': ferti})


def bio_fertilizer(request):
    bio = Bio_Fertilizer.objects.all()
    return render(request, 'bio-fertilizer.html', {'bio': bio})


def seed_treatment(request):
    seed = Seed_Treatment.objects.all()
    return render(request, 'seed_treatment.html', {'seed': seed})


def equipment(request):
    equip = Equipment.objects.all()
    return render(request, 'equipment.html', {'equip': equip})
