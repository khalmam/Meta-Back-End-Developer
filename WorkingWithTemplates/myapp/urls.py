from django.urls import path
from . import views

urlpatterns = [
    #path('menu_card/', views.menu_by_id),
    path('home/', views.home),
     path('about/', views.about),
      path('menu/', views.menu),
      path('book/', views.book),
]