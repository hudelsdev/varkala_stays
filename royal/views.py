import logging
from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.http import HttpResponse
import json
import os
import random
import string
from django.conf import settings
from urllib.parse import urlencode
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import Table,TableStyle

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
                    ['sales@hudels.com'],
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



# voucher cretions views 

def generate_booking_reference():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))


def voucher_create_index(request):
        booking_reference = generate_booking_reference()
        context = {
            'booking_reference': booking_reference
        }
        return render(request, 'voucher_index.html', context)



def create_customer_voucher(request):
    if request.method == 'POST':
        booking_reference = request.POST.get('booking_reference')
        voucher_data = {
            'booking_reference': booking_reference,
            'booking_status': request.POST.get('booking_status'),
            'payment_status': request.POST.get('payment_status'),
            'customer_name': request.POST.get('customer_name'),
            'hotel_name': request.POST.get('hotel_name'),
            'room_type': request.POST.get('room_type'),
            'number_of_nights': request.POST.get('number_of_nights'),
            'number_of_rooms': request.POST.get('number_of_rooms'),
            'adults': request.POST.get('adults'),
            'children': request.POST.get('children'),
            'hotel_contact_number': request.POST.get('hotel_contact_number'),
            'meal_plan': request.POST.get('meal_plan'),
            'arrival_details': request.POST.get('arrival_details'),
            'total_booking_amount': request.POST.get('total_booking_amount'),
            'advance_amount': request.POST.get('advance_amount'),
            'balance_payable': request.POST.get('balance_payable'),
            'check_in_time': request.POST.get('check_in_time'),
            'check_out_time': request.POST.get('check_out_time'),
            'remarks': request.POST.get('remarks'),
        }

        # save_voucher(voucher_data)
        query_string = urlencode(voucher_data)
        return redirect(f'/success/?{query_string}')

    return render(request, 'create_customer_voucher.html')



def create_hotel_voucher(request):
    if request.method == 'POST':
        booking_reference = request.POST.get('booking_reference')
        voucher_data = {
            'booking_reference': booking_reference,
            'booking_status': request.POST.get('booking_status'),
            'payment_status': request.POST.get('payment_status'),
            'customer_name': request.POST.get('customer_name'),
            'hotel_name': request.POST.get('hotel_name'),
            'room_type': request.POST.get('room_type'),
            'number_of_nights': request.POST.get('number_of_nights'),
            'number_of_rooms': request.POST.get('number_of_rooms'),
            'adults': request.POST.get('adults'),
            'children': request.POST.get('children'),
            'hotel_contact_number': request.POST.get('hotel_contact_number'),
            'meal_plan': request.POST.get('meal_plan'),
            'arrival_details': request.POST.get('arrival_details'),
            'total_booking_amount': request.POST.get('total_booking_amount'),
            'commission_amount': request.POST.get('commission_amount'),
            'net_hotel_amount': request.POST.get('net_hotel_amount'),
            'check_in_date': request.POST.get('check_in_date'),
            'check_out_date': request.POST.get('check_out_date'),
            'amount_collected_from_customer': request.POST.get('amount_collected_from_customer'),
            'balance_to_collect': request.POST.get('balance_to_collect'),
            'remarks': request.POST.get('remarks'),
        }

        # save_voucher(voucher_data)
        query_string = urlencode(voucher_data)
        return redirect(f'/success/?{query_string}')

    return render(request, 'create_hotel_voucher.html')



def voucher_success(request):
    voucher_data = request.GET.get('voucher_data')
    return render(request, 'voucher_success.html', {'voucher_data': voucher_data})



# def save_voucher(voucher_data):
#     vouchers_file_path = os.path.join(settings.BASE_DIR, 'vouchers_data.json')

#     if os.path.exists(vouchers_file_path):
#         with open(vouchers_file_path, 'r') as file:
#             vouchers = json.load(file)
#     else:
#         vouchers = []

#     vouchers.append(voucher_data)

#     with open(vouchers_file_path, 'w') as file:
#         json.dump(vouchers, file, indent=4)



def download_voucher(request, voucher_type):
    voucher_data = request.GET.dict()

    response = HttpResponse(content_type='application/pdf')
    if voucher_type == 'customer':
        response['Content-Disposition'] = 'attachment; filename="customer_voucher.pdf"'
        create_customer_voucher_pdf(response, voucher_data)
    elif voucher_type == 'hotel':
        response['Content-Disposition'] = 'attachment; filename="hotel_voucher.pdf"'
        create_hotel_voucher_pdf(response, voucher_data)

    return response



def create_customer_voucher_pdf(response, voucher_data):
    p = canvas.Canvas(response, pagesize=letter)
    width, height = letter
    
     #  border around the page
     
    p.setLineWidth(2)
    p.setStrokeColor(colors.darkgreen)
    p.rect(20, 20, width-40, height-40)
    
    
    # logo
    logo_path = os.path.join(settings.BASE_DIR, 'static/image/varkala_logo.png')
    if os.path.exists(logo_path):
        p.drawImage(logo_path, 40, height - 180, width=50, preserveAspectRatio=True, mask='auto')
    else:
        print(f"Logo not found at {logo_path}")
        p.setFillColor(colors.red)
        p.setFont("Helvetica-Bold", 12)
        p.drawString(40, height - 100, "Logo not found")


    #  styles
    p.setFont("Helvetica-Bold", 16)
    p.setFillColor(colors.darkgreen)
    p.drawString(200, height - 40, "Customer Voucher")
    
      # Subheading
    p.setFont("Helvetica", 14)
    p.setFillColor(colors.black)
    p.drawString(150, height - 70, "GO ROOMS BOOKING CONFIRMATION")
    
    
    # line
    p.setLineWidth(1)
    p.line(40, height - 80, width - 40, height - 80)

    p.setFont("Helvetica", 12)
    p.setFillColor(colors.black)

    x = 40
    y = height - 550
    
    

        
    #  data for the table
    
    data = [["BOOKING REFERENCE", voucher_data.get('booking_reference')],
            ["BOOKING STATUS", voucher_data.get('booking_status')],
            ["PAYMENT STATUS", voucher_data.get('payment_status')],
            ["CUSTOMER NAME", voucher_data.get('customer_name')],
            ["HOTEL NAME", voucher_data.get('hotel_name')],
            ["ROOM TYPE", voucher_data.get('room_type')],
            ["NUMBER OF NIGHTS", voucher_data.get('number_of_nights')],
            ["NUMBER OF ROOMS", voucher_data.get('number_of_rooms')],
            ["ADULTS", voucher_data.get('adults')],
            ["CHILDREN", voucher_data.get('children')],
            ["HOTEL CONTACT NUMBER", voucher_data.get('hotel_contact_number')],
            ["MEAL PLAN", voucher_data.get('meal_plan')],
            ["ARRIVAL DETAILS", voucher_data.get('arrival_details')],
            ["TOTAL BOOKING AMOUNT", voucher_data.get('total_booking_amount')],
            ["ADVANCE AMOUNT", voucher_data.get('advance_amount')],
            ["BALANCE PAYABLE", voucher_data.get('balance_payable')],
            ["CHECK-IN DATE", voucher_data.get('check_in_date')],
            ["CHECK-OUT DATE", voucher_data.get('check_out_date')],
            ["CHECK-IN TIME", voucher_data.get('check_in_time')],
            ["CHECK-OUT TIME", voucher_data.get('check_out_time')],
            ]

    # Create table
    col_widths = [155, width - 225]
    table = Table(data,colWidths=col_widths)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.white),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 22),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    
    
    # Separate the remarks into a box

    remarks = voucher_data.get('remarks', '')
    if remarks:
        remarks_box_x = 40
        remarks_box_y = y - 60  
        remarks_box_width = width - 80
        remarks_box_height = 50  
        
        p.setFillColor(colors.white)
        p.rect(remarks_box_x, remarks_box_y, remarks_box_width, remarks_box_height, fill=1)
        p.setFillColor(colors.black)
        p.setFont("Helvetica", 12)
        p.drawString(remarks_box_x + 10, remarks_box_y + 30, "Remarks:")
        p.setFont("Helvetica", 10)
        p.drawString(remarks_box_x + 10, remarks_box_y + 10, remarks)

    #  table on the PDF
    table.wrapOn(p, width, height)
    table.drawOn(p, x, y)
       
    
    # confirmation_box
 
    confirmation_box_x = width - 300
    confirmation_box_y = height - 150
    p.setFillColor(colors.white)
    p.rect(confirmation_box_x, confirmation_box_y, 270, 50, fill=1)

    tick_mark_path = os.path.join(settings.BASE_DIR, 'static/image/image001.png')
    if os.path.exists(tick_mark_path):
        p.drawImage(tick_mark_path, confirmation_box_x + 10, confirmation_box_y + 0, width=50, height=50, mask='auto')

    p.setFillColor(colors.black)
    p.setFont("Helvetica-Bold", 10)
    p.drawString(confirmation_box_x + 60, confirmation_box_y + 25, "Your Booking is Confirmed")
    
    
    
 # Add contact details below the table
    contact_text = """Cancellation Policy: No charges if cancelled before 7 Days of Check In. 50% charges if cancelled before 72 hours of 
    Check In, No refund for any cancellation done within 72 hours of Check in Date
    For any further assistance please contact our support team.
    Contact Customer Care - +91-9353811748 (10:00 am – 10:00 pm)
    For Refunds & Finance related – finance@varkalastays.com
    For Other Requests - sales@varkalastays.comVarkala Stays, Go Rooms by Hudels Hospitality Services Pvt Ltd"""

    p.setFont("Helvetica", 10)
    text_x = 40
    text_y = 125  # Adjust position to ensure it is below the table
    for line in contact_text.split("\n"):
        p.drawString(text_x, text_y, line)
        text_y -= 15
    p.showPage()
    p.save()



def create_hotel_voucher_pdf(response, voucher_data):
    p = canvas.Canvas(response, pagesize=letter)
    width, height = letter
    
     #  border around the page
    p.setLineWidth(2)
    p.setStrokeColor(colors.darkgreen)
    p.rect(20, 20, width-40, height-40)
    
    
    # logo
    logo_path = os.path.join(settings.BASE_DIR, 'static/image/varkala_logo.png')
    if os.path.exists(logo_path):
        p.drawImage(logo_path, 40, height - 180, width=50, preserveAspectRatio=True, mask='auto')
    else:
        print(f"Logo not found at {logo_path}")
        p.setFillColor(colors.red)
        p.setFont("Helvetica-Bold", 12)
        p.drawString(40, height - 100, "Logo not found")
        
        
    #  styles
    p.setFont("Helvetica-Bold", 16)
    p.setFillColor(colors.darkgreen)
    p.drawString(200, height - 40, "Hotel Official Voucher")
    
    
        
      # Subheading
    p.setFont("Helvetica", 14)
    p.setFillColor(colors.black)
    p.drawString(150, height - 70, "GO ROOMS BOOKING CONFIRMATION")
    
    
    # line
    p.setLineWidth(1)
    p.line(40, height - 80, width - 40, height - 80)

    p.setFont("Helvetica", 12)
    p.setFillColor(colors.black)

    x = 40
    y = height - 550
    
    
     # Separate the remarks into a box
     
    remarks = voucher_data.get('remarks', '')
    if remarks:
        remarks_box_x = 40
        remarks_box_y = y - 60  
        remarks_box_width = width - 80
        remarks_box_height = 50  
        
        p.setFillColor(colors.white)
        p.rect(remarks_box_x, remarks_box_y, remarks_box_width, remarks_box_height, fill=1)
        p.setFillColor(colors.black)
        p.setFont("Helvetica", 12)
        p.drawString(remarks_box_x + 10, remarks_box_y + 30, "Remarks:")
        p.setFont("Helvetica", 10)
        p.drawString(remarks_box_x + 10, remarks_box_y + 10, remarks)
        
    
    #  data for the table
    data = [["BOOKING REFERENCE", voucher_data.get('booking_reference')],
            ["BOOKING STATUS", voucher_data.get('booking_status')],
            ["PAYMENT STATUS", voucher_data.get('payment_status')],
            ["CUSTOMER NAME", voucher_data.get('customer_name')],
            ["ROOM TYPE", voucher_data.get('room_type')],
            ["NUMBER OF NIGHTS", voucher_data.get('number_of_nights')],
            ["NUMBER OF ROOMS", voucher_data.get('number_of_rooms')],
            ["ADULTS", voucher_data.get('adults')],
            ["CHILDREN", voucher_data.get('children')],
            ["CUSTOMER CONTACT NUMBER", voucher_data.get('customer_contact_number')],
            ["MEAL PLAN", voucher_data.get('meal_plan')],
            ["ARRIVAL DETAILS", voucher_data.get('arrival_details')],
            ["TOTAL BOOKING AMOUNT", voucher_data.get('total_booking_amount')],
            ["COMMISSION AMOUNT", voucher_data.get('commission_amount')],
            ["NET HOTEL AMOUNT", voucher_data.get('net_hotel_amount')],
            ["CHECK-IN DATE", voucher_data.get('check_in_date')],
            ["CHECK-OUT DATE", voucher_data.get('check_out_date')],
            ["COLLECTED AMOUNT", voucher_data.get('amount_collected_from_customer')],
            ["BALANCE TO COLLECT", voucher_data.get('balance_to_collect')],
            ]

    # Create table
    col_widths = [155, width - 225]
    table = Table(data,colWidths=col_widths)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.white),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 22),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    #  table on the PDF
    table.wrapOn(p, width, height)
    table.drawOn(p, x, y)

    # confirmation_box
 
    confirmation_box_x = width - 300
    confirmation_box_y = height - 145
    p.setFillColor(colors.white)
    p.rect(confirmation_box_x, confirmation_box_y, 250, 50, fill=1)

    tick_mark_path = os.path.join(settings.BASE_DIR, 'static/image/image001.png')
    if os.path.exists(tick_mark_path):
        p.drawImage(tick_mark_path, confirmation_box_x + 10, confirmation_box_y + 0, width=50, height=50, mask='auto')

    p.setFillColor(colors.black)
    p.setFont("Helvetica-Bold", 10)
    p.drawString(confirmation_box_x + 60, confirmation_box_y + 25, "Your Booking is Confirmed")
    
    
 # Add contact details below the table
    contact_text = """For any further assistance please contact our support team.For invoice related, contact finance@hudels.com
    sales@hudels.com
    Contact Akhil Prakash on 9074582622
    Varkala Stays by Hudels Hospitality Services"""

    p.setFont("Helvetica", 10)
    text_x = 40
    text_y = 130  # Adjust position to ensure it is below the table 
    for line in contact_text.split("\n"):
        p.drawString(text_x, text_y, line)
        text_y -= 15
        
    
    
    p.showPage()
    p.save()
