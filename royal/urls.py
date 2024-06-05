from django.urls import path 
from .views import *

urlpatterns =[
    path('',varkala_index,name='index'),
    path('about/',varkala_about,name='about'),
    path('gallery/',varkala_gallery,name='gallery'),
    path('property_list/',varkala_list,name='property_list'),
    path('contact/',varkala_contact,name='contact'),

    #modifiy on 23/05/2024 -- chandru 
    # path('ashokam/',ashokam_details,name='ashokam_details'),

    # modifiy on 21/05/2024 -- chandru 

    # path('accomodation/',varkala_accomodation,name='accomodation'),
    # path('blog-single/',varkala_blog_single,name='blog-single'),
    
    
    # modifiy on 21/05/2024 -- chandru 
    path('ashokam/',ashokam_details,name='ashokam_details'),
    path('cliffcounty/',cliffcounty_details,name='cliffcounty_details'),
    path('evebeach/',eva_beach_details,name='evebeach_details'),
    path('haiwa/',haiwa_details,name='haiwa_details_details'),
    path('skyframe/',skyframe_details,name='skyframe_details'),
    path('nisara/',nisara_details,name='nisara_details'),
    path('moon_waves/',moon_waves_details,name='moon_waves_details'),
    path('villa_skyframe/',villa_skyframe_details,name='villa_skyframe_details'),

]