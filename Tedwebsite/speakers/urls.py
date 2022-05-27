from django.urls import path
from . import views

urlpatterns = [
    path('', views.speakers_home, name='speakers_home'),
    path('/speakers.html', views.nominate_others),
    path('/form2.html', views.nominate_yourself),
    path('/blog.html', views.blogs),
    path('/about_us.html', views.about_us),
    path('/contact.html', views.contact),

    
    path('/speakers.html/form2.html', views.nominate_yourself),
    path('/speakers.html/speakers.html', views.nominate_others),
    path('/speakers.html/blog.html', views.blogs),
    path('/speakers.html/about_us.html', views.about_us),
    path('/contact.html', views.contact),

    
    path('/Alana_Golmei', views.speakerDesc1, name='speaker_description1'),
    path('/Anamika_Barua', views.speakerDesc2, name='speaker_description2'),
    path('/Arup_Kumar_Dutta', views.speakerDesc3, name='speaker_description3'),
    path('/Binita_Jain', views.speakerDesc4, name='speaker_description4'),
    path('/Milin_Dutta', views.speakerDesc5, name='speaker_description5'),
    path('/Zoma_Sailo', views.speakerDesc6, name='speaker_description6'),
    path('/Pragnya_Ramjee', views.speakerDesc7, name='speaker_description7'),

    path('/Seema_Biswas', views.speakerDesc8, name='speaker_description8'),
    path('/Uddhab_Bharali', views.speakerDesc9, name='speaker_description9'),
    path('/Sankara_Subramaniam', views.speakerDesc10, name='speaker_description10'),
    path('/Hasina_Kharbhih', views.speakerDesc11, name='speaker_description11'),
    path('/Sonjoy_Hazarika', views.speakerDesc12, name='speaker_description12'),
    path('/Ravindranath_Ravi', views.speakerDesc13, name='speaker_description13'),

    path('/Aashish_Chandratreya', views.speakerDesc14, name='speaker_description14'),
    path('/Aditya_Gupta', views.speakerDesc15, name='speaker_description15'),
    path('/Bhagvan_Kommadi', views.speakerDesc16, name='speaker_description16'),
    path('/Bidisha_Som', views.speakerDesc17, name='speaker_description17'),
    path('/Nisha_Bora', views.speakerDesc18, name='speaker_description18'),
    path('/Prabhagaran', views.speakerDesc19, name='speaker_description19'),
    path('/Rudy_Wallang', views.speakerDesc20, name='speaker_description20'),
    path('/Seema_Gupta', views.speakerDesc21, name='speaker_description21'),
    path('/Shiva_Sah', views.speakerDesc22, name='speaker_description22'),

    path('/jalal.html', views.speakerDesc44, name='speaker_description44'),
    path('/Magician.html', views.speakerDesc45, name='speaker_description45'),
    path('/parvathy.html', views.speakerDesc46, name='speaker_description46'),
    path('/abhimanyu.html', views.speakerDesc47, name='speaker_description47'),
    path('/rishab_mandeep.html', views.speakerDesc48, name='speaker_description48'),
    path('/Rohan.html', views.speakerDesc49, name='speaker_description49'),
    path('/saumya.html', views.speakerDesc50, name='speaker_description50'),
    path('/james.html', views.speakerDesc51, name='speaker_description51'),
 
    path('/speakers.html/Alana_Golmei', views.speakerDesc1, name='speaker_description1'),
    path('/speakers.html/Anamika_Barua', views.speakerDesc2, name='speaker_description2'),
    path('/speakers.html/Arup_Kumar_Dutta', views.speakerDesc3, name='speaker_description3'),
    path('/speakers.html/Binita_Jain', views.speakerDesc4, name='speaker_description4'),
    path('/speakers.html/Milin_Dutta', views.speakerDesc5, name='speaker_description5'),
    path('/speakers.html/Zoma_Sailo', views.speakerDesc6, name='speaker_description6'),
    path('/speakers.html/Pragnya_Ramjee', views.speakerDesc7, name='speaker_description7'),

    path('/speakers.html/Seema_Biswas', views.speakerDesc8, name='speaker_description8'),
    path('/speakers.html/Uddhab_Bharali', views.speakerDesc9, name='speaker_description9'),
    path('/speakers.html/Sankara_Subramaniam', views.speakerDesc10, name='speaker_description10'),
    path('/speakers.html/Hasina_Kharbhih', views.speakerDesc11, name='speaker_description11'),
    path('/speakers.html/Sonjoy_Hazarika', views.speakerDesc12, name='speaker_description12'),
    path('/speakers.html/Ravindranath_Ravi', views.speakerDesc13, name='speaker_description13'),

    path('/speakers.html/Aashish_Chandratreya', views.speakerDesc14, name='speaker_description14'),
    path('/speakers.html/Aditya_Gupta', views.speakerDesc15, name='speaker_description15'),
    path('/speakers.html/Bhagvan_Kommadi', views.speakerDesc16, name='speaker_description16'),
    path('/speakers.html/Bidisha_Som', views.speakerDesc17, name='speaker_description17'),
    path('/speakers.html/Nisha_Bora', views.speakerDesc18, name='speaker_description18'),
    path('/speakers.html/Prabhagaran', views.speakerDesc19, name='speaker_description19'),
    path('/speakers.html/Rudy_Wallang', views.speakerDesc20, name='speaker_description20'),
    path('/speakers.html/Seema_Gupta', views.speakerDesc21, name='speaker_description21'),
    path('/speakers.html/Shiva_Sah', views.speakerDesc22, name='speaker_description22'),
   
#    the linking of the speakers of studio 2021-22

    path('/speakers.html/VR_Raman', views.speakerDesc100, name='speaker_description100'),
    path('/speakers.html/Binayak_Acharya', views.speakerDesc101, name='speaker_description101'),
    path('/speakers.html/Helia_Singh', views.speakerDesc102, name='speaker_description102'),
    path('/speakers.html/Akshita', views.speakerDesc103, name='speaker_description100'),

   path('/about_us.html/Jaikishan_Mansukhani', views.memberDesc1, name='member_description1'),
    path('/about_us.html/Anvita_Kodru', views.memberDesc2, name='member_description2'),
    path('/about_us.html/Sreesiddesh_Bhavanasi', views.memberDesc3, name='member_description3'),
    path('/about_us.html/Shivangi_Kumar', views.memberDesc4, name='member_description4'),
    path('/about_us.html/Vishwaprasanna_Hariharan', views.memberDesc5, name='member_description5'),
    path('/about_us.html/Samarth_Saraswat', views.memberDesc6, name='member_description6'),
    path('/about_us.html/Aarya_Shrivastava', views.memberDesc7, name='member_description7'),
    path('/about_us.html/Amey_Varhade', views.memberDesc8, name='member_description8'),
    path('/about_us.html/Anindya_Rajan', views.memberDesc9, name='member_description9'),
    path('/about_us.html/Anisha_Khati', views.memberDesc10, name='member_description10'),
    path('/about_us.html/Ankit_Raj', views.memberDesc11, name='member_description11'),
    path('/about_us.html/Anushka_Anand', views.memberDesc12, name='member_description12'),
    path('/about_us.html/Anushka_Srivastava', views.memberDesc13, name='member_description13'),
    path('/about_us.html/Arpita_Mohapatra', views.memberDesc14, name='member_description14'),
    path('/about_us.html/Ayush_Srivastava', views.memberDesc15, name='member_description15'),
    path('/about_us.html/Digisha_Verma', views.memberDesc16, name='member_description16'),
    path('/about_us.html/Emily_Huiling', views.memberDesc17, name='member_description17'),
    path('/about_us.html/Gourav_Kumar', views.memberDesc18, name='member_description18'),
    path('/about_us.html/Govind_Singh', views.memberDesc19, name='member_description19'),
    path('/about_us.html/Jaideep_Buksagarmath', views.memberDesc20, name='member_description20'),
    path('/about_us.html/Janhavi_Lande', views.memberDesc21, name='member_description21'),
    path('/about_us.html/Lalika_Laya_K', views.memberDesc22, name='member_description22'),
    path('/about_us.html/Miloni_Patel', views.memberDesc23, name='member_description23'),
    path('/about_us.html/Monalisha_Majumder', views.memberDesc24, name='member_description24'),
    path('/about_us.html/Niladri_Sarkar', views.memberDesc25, name='member_description25'),
    path('/about_us.html/Nishant', views.memberDesc26, name='member_description26'),
    path('/about_us.html/Nishtha_Sharma', views.memberDesc27, name='member_description27'),
    path('/about_us.html/Pragnya_Ramjee', views.memberDesc28, name='member_description28'),
    path('/about_us.html/Pratyanshu_Raj_Singh', views.memberDesc29, name='member_description29'),
    path('/about_us.html/Ritik_Singh', views.memberDesc30, name='member_description30'),
    path('/about_us.html/Sai_Sreyas_Ray', views.memberDesc31, name='member_description31'),
    path('/about_us.html/Shatakshi_Kaushal', views.memberDesc32, name='member_description32'),
    path('/about_us.html/Shiva_Sah', views.memberDesc33, name='member_description33'),
    path('/about_us.html/Sudarshan_Birla', views.memberDesc34, name='member_description34'),
    path('/about_us.html/Titiksha', views.memberDesc35, name='member_description35'),


    # path('add_speaker', views.addSpeaker),

    # Linking of event speakers


]
