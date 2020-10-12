from django.shortcuts import render


# Create your views here.

def post_list(request):
    return render(request, 'firstapp/post_list.html', {})


def about_page(requst):
    return render(requst, 'firstapp/about.html')
