from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.index, name='home'),
    path('product', views.product, name='product'),
    path('pesticide', views.pesticide, name='pesticide'),
    path('insecticide', views.insecticide, name='insecticide'),
    path('herbicide', views.herbicide, name='herbicide'),
    path('fungicide', views.fungicide, name='fungicide'),
    path('fertilizer', views.fertilizer, name='fertilizer'),
    path('bio_fertilizer', views.bio_fertilizer, name='bio_fertilizer'),
    path('seed_treatment', views.seed_treatment, name='seed_treatment'),
    path('equipment', views.equipment, name='equipment'),
]
