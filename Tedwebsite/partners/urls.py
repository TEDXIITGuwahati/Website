from django.urls import path
from . import views
urlpatterns = [

    
    path('/', views.partners),
    path('/about_us.html', views.about_us),
    path('/contact.html', views.contact),

]