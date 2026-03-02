from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import RegistratieForm
from .models import SearchQuery, Zaak


def home(request):
    return redirect('zoek') if request.user.is_authenticated else redirect('login')


def registreer(request):
    if request.method == 'POST':
        form = RegistratieForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('zoek')
    else:
        form = RegistratieForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def zoek(request):
    query = request.GET.get('q', '').strip()
    onderwerp = request.GET.get('onderwerp', '').strip()
    dictum = request.GET.get('dictum', '').strip()

    resultaten = Zaak.objects.all()

    if query:
        for term in query.split():
            resultaten = resultaten.filter(advies_tekst__icontains=term)

    if onderwerp:
        resultaten = resultaten.filter(onderwerp__icontains=onderwerp)

    if dictum:
        resultaten = resultaten.filter(dictum__icontains=dictum)

    if query:
        SearchQuery.objects.create(
            gebruiker=request.user,
            zoekterm=query,
            onderwerp_filter=onderwerp,
            dictum_filter=dictum,
            resultaten_telling=resultaten.count(),
        )

    context = {
        'resultaten': resultaten[:50],
        'query': query,
        'onderwerp': onderwerp,
        'dictum': dictum,
    }
    return render(request, 'adviezen/zoek.html', context)


@login_required
def zoekhistorie(request):
    historie = SearchQuery.objects.filter(gebruiker=request.user)[:25]
    return render(request, 'adviezen/zoekhistorie.html', {'historie': historie})
