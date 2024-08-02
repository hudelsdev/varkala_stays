from django.urls import path 
from .views import *

urlpatterns =[
    path('',varkala_index,name='index'),
    path('about/',varkala_about,name='about'),
    path('gallery/',varkala_gallery,name='gallery'),
    path('property_list/',varkala_list,name='property_list'),
    path('contact/',varkala_contact,name='contact'),
    path('enquiry/',send_enquiry_email,name='enquiry'),
    path('enquirysuccess/',enquirysuccess,name='enquirysuccess'),

    
    path('ashokam/',ashokam_details,name='ashokam_details'),
    path('cliffcounty/',cliffcounty_details,name='cliffcounty_details'),
    path('evabeach/',eva_beach_details,name='evabeach_details'),
    path('haiwa/',haiwa_details,name='haiwa_details_details'),
    path('skyframe/',skyframe_details,name='skyframe_details'),
    path('nisara/',nisara_details,name='nisara_details'),
    path('moon_waves/',moon_waves_details,name='moon_waves_details'),
    path('varkalastays_premium_by_hudels/',varkalastays_premium_by_hudels_details,name='varkalastays_premium_by_hudels_details'),
    path('villa_skyframe/',villa_skyframe_details,name='villa_skyframe_details'), 
    path('ss_beach_resort/',ss_beach_resort_details,name='ss_beach_resort_details'),
    path('zion_villa_resort/',zion_villa_resort_details,name='zion_villa_resort_details'),
    path('gone_costal/',gone_costal_details,name='gone_costal_details'),
    path('kerala_bamboo/',kerala_bamboo_details,name='kerala_bamboo_details'),
    path('urban_cliff/',urban_cliff_details,name='urban_cliff_details'),
    path('pearl_beach_resort/',pearl_beach_resort_details,name='pearl_beach_resort_details'),
    path('varkala_villa/',varkala_villa_details,name='varkala_villa_details'),
    path('pura_vida/',pura_vida_details,name='pura_vida_details'),
    
        # voucher creations urls
    
    # path('voucher_create_index/', voucher_create_index, name='voucher_create_index'),
    # path('create_customer_voucher/', create_customer_voucher, name='create_customer_voucher'),
    # path('create_hotel_voucher/', create_hotel_voucher, name='create_hotel_voucher'),
    # path('success/', voucher_success, name='voucher_success'),
    # path('download/<str:voucher_type>/', download_voucher, name='download_voucher'),
]
