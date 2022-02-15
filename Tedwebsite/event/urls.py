from django.urls import path
from . import views
urlpatterns = [

    
    path('/', views.events),
    path('/speakers.html/jalal.html', views.speakerDesc44, name='speaker_description44'),
    path('/speakers.html/Magician.html', views.speakerDesc45, name='speaker_description45'),
    path('/speakers.html/parvathy.html', views.speakerDesc46, name='speaker_description46'),
    path('/speakers.html/abhimanyu.html', views.speakerDesc47, name='speaker_description47'),
    path('/speakers.html/rishab_mandeep.html', views.speakerDesc48, name='speaker_description48'),
    path('/speakers.html/Rohan.html', views.speakerDesc49, name='speaker_description49'),
    path('/speakers.html/saumya.html', views.speakerDesc50, name='speaker_description50'),
    path('/speakers.html/james.html', views.speakerDesc51, name='speaker_description51'),


]