from django.shortcuts import render


FEATURES = [
    {'title': 'Samenwerken', 'description': 'Werk samen met je team in één gedeelde omgeving.'},
    {'title': 'Automatiseren', 'description': 'Automatiseer terugkerende taken en bespaar tijd.'},
    {'title': 'Inzicht', 'description': 'Krijg real-time dashboards en rapportages.'},
]


def home(request):
    context = {
        'platform_name': 'FlowPlatform',
        'hero_title': 'Bouw sneller met één modern platform',
        'hero_subtitle': 'Beheer projecten, communicatie en processen op één plek.',
        'features': FEATURES,
    }
    return render(request, 'core/home.html', context)
