from django.shortcuts import render

from web_app.forms import SongForm


def basic_web_app(request):
    ctx = {}
    ctx['albums'] = [
        {
            'artist': 'Les Gordon',
            'title': 'Abyss',
            'year': '2016',
            'songs': [
                {
                    'track': 1,
                    'title': 'Abyss',
                    'duration': '3:13'
                },
                {
                    'track': 2,
                    'title': 'Shiho & Kyoko',
                    'duration': '2:58'
                },
            ]
        },
        {
            'artist': 'Same Gellaitry',
            'title': 'Escapism II',
            'year': '2016',
            'songs': [
                {
                    'track': 1,
                    'title': 'The Gateway',
                    'duration': '3:12'
                },
                {
                    'track': 2,
                    'title': 'Desert Mirage',
                    'duration': '5:00'
                },
                {
                    'track': 3,
                    'title': 'Jacket Weather',
                    'duration': None
                },
                {
                    'track': 4,
                    'title': 'Static Sleep',
                    'duration': ''
                }
            ]
        }
    ]
    template_name = 'web_app/basic.html'
    return render(request, template_name, ctx)


def dynamic_web_app(request):
    ctx = {}
    template_name = 'web_app/dynamic.html'
    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            ctx['song'] = form.cleaned_data
    else:
        form = SongForm()
    ctx['form'] = form
    return render(request, template_name, ctx)
