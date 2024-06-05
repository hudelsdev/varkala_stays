from django.shortcuts import render

# Create your views here.
def varkala_index(request):
    return render(request, "index.html")

def varkala_about(request):
    return render(request, "about.html")

def varkala_gallery(request):
    return render(request, "gallery.html")

def varkala_contact(request):
    return render(request, "contact.html")

#   # modifiy on 04/06/2024 -- chandru 


def varkala_list(request):
    return render(request, "property_list.html")

#hotels list


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
# modifiy on 21/05/2024 -- chandru 

# def varkala_accomodation(request):
#     return render(request, "accomodation.html")

# def varkala_blog(request):
#     return render(request, "blog.html")

# def varkala_blog_single(request):
#     return render(request, "blog-single.html")
