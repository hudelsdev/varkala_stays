import logging
from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.http import HttpResponse
import os
from django.conf import settings
from urllib.parse import urlencode


logger = logging.getLogger(__name__)

# Create your views here.

def varkala_index(request):
    return render(request, "index.html")


def varkala_about(request):
    return render(request, "about.html")


def varkala_gallery(request):
    return render(request, "gallery.html")


def varkala_contact(request):
    return render(request, "contact.html")



def enquirysuccess(request):
    return render(request, "success.html")


def send_enquiry_email(request):
    if request.method == 'POST':
        check_in = request.POST.get('check_in')
        check_out = request.POST.get('check_out')
        name = request.POST.get('name')
        contact_number = request.POST.get('contact_number') 
        num_people = request.POST.get('num_people')
        
        print("Received data:", check_in, check_out, name, contact_number, num_people)
        
        if check_in and check_out and name and contact_number and num_people:
            try:
                send_mail(
                    'New Enquiry',
                    f'Check-in date: {check_in}\nCheck-out date: {check_out}\n'
                    f'Name: {name}\nContact number: {contact_number}\nNumber of people: {num_people}',
                    None,  
                    ['varkalastays@gmail.com'],
                    fail_silently=False,
                )
                print("Email sent successfully")
                
                return redirect('enquirysuccess')
            except Exception as e: 
                logger.error(f"Error sending email: {e}")
                return HttpResponse(f"Error sending email: {e}", status=500)
        else:
            return HttpResponse("All fields are required", status=400)

    return render(request, 'contact.html')


#hotels list
def varkala_list(request):
    return render(request, "property_list.html")


#hotel details
def ashokam_details(request):
    return render(request, "ashokam_details.html")


def eva_beach_details(request):
    return render(request, "evabeach_details.html")


def haiwa_details(request):
    return render(request, "haiwa_details.html")


def skyframe_details(request):
    return render(request, "skyframe_details.html")


def nisara_details(request):
    return render(request, "nisara_details.html")


def moon_waves_details(request):
    return render(request, "moon_waves_details.html")


def villa_skyframe_details(request):
    return render(request, "villa_skyframe_details.html")
 
 
def cliffcounty_details(request):
    return render(request, "cliffcounty_details.html")

def varkalastays_premium_by_hudels_details(request):
    return render(request, "varkalastays_premium_by_hudels.html")


def ss_beach_resort_details(request):
    return render(request, "ss_beach_resort.html")


def zion_villa_resort_details(request):
    return render(request, "zion_villa_resort.html")


def gone_costal_details(request):
    return render(request, "gone_costal.html")


def kerala_bamboo_details(request):
    return render(request, "kerala_bamboo.html")


def urban_cliff_details(request):
    return render(request, "urban_cliff.html")


def pearl_beach_resort_details(request):
    return render(request, "pearl_beach_resort.html")


def varkala_villa_details(request):
    return render(request, "varkala_villa.html")


def pura_vida_details(request):
    return render(request, "pura_vida.html")

# voucher cretions views 


