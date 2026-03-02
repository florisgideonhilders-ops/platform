from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse

from .models import SearchQuery, Zaak


class ZoekFlowTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='jurist', password='test12345')
        Zaak.objects.create(
            octopus_zaaknummer='Z-001',
            onderwerp='Contract',
            dictum='Toegewezen',
            advies_tekst='Dit advies gaat over contractuele aansprakelijkheid.',
        )
        Zaak.objects.create(
            octopus_zaaknummer='Z-002',
            onderwerp='Arbeid',
            dictum='Afgewezen',
            advies_tekst='Dit advies behandelt ontslag en arbeidsvoorwaarden.',
        )

    def test_zoek_slaat_query_op(self):
        client = Client()
        client.login(username='jurist', password='test12345')

        response = client.get(reverse('zoek'), {'q': 'contract'})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(SearchQuery.objects.count(), 1)
        self.assertEqual(SearchQuery.objects.first().zoekterm, 'contract')

    def test_zoekhistorie_vereist_login(self):
        response = self.client.get(reverse('zoekhistorie'))
        self.assertEqual(response.status_code, 302)
