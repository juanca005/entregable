from django.urls import path

from familiar.views import create_familiar,list_familiar


urlpatterns = [
    path('create-familiar/', create_familiar),
    path('list-familiar/', list_familiar)
]