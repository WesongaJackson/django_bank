from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'main_app/index.html')


def about(request):
    return render(request, 'main_app/about.html')


def blog(request):
    return render(request, 'main_app/blog.html')


def blog_details(request):
    return render(request, 'main_app/blog-details.html')


def how_it_works(request):
    return render(request, 'main_app/how-it-works.html')


def legal(request):
    return render(request, 'main_app/legal.html')


def terms(request):
    return render(request, 'main_app/terms.html')


def services(request):
    return render(request, 'main_app/services.html')


def services_detail(request):
    return render(request, 'main_app/service-details.html')


def contact(request):
    return render(request, 'main_app/contact.html')


def faq(request):
    return render(request, 'main_app/faq.html')


def privacy_policy(request):
    return render(request, 'main_app/privacy-policy.html')
