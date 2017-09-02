from django.shortcuts import render


def basic_web_page(request):
    ctx = {}
    template_name = 'web_pages/basic.html'
    return render(request, template_name, ctx)
