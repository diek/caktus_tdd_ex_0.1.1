from django.urls import path

from . import views

urlpatterns = [
    path('drill/', views.drill, name='drill'),
    path('answer/', views.answer, name='answer')
]
