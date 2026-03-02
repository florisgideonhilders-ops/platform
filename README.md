# Juridisch Zoekportaal

Herbouwde basis van de gedeelde ChatGPT-conversatie: een Django-app waarin juristen kunnen inloggen, adviezen doorzoeken en zoekgeschiedenis opslaan.

## Functionaliteiten

- Inloggen/uitloggen via Django auth.
- Registratiepagina voor nieuwe gebruikers.
- Model `Zaak` voor adviezen.
- Zoekpagina met tekstzoeking en eenvoudige filters (`onderwerp`, `dictum`).
- Model `SearchQuery` om zoekopdrachten per gebruiker op te slaan.
- Pagina met persoonlijke zoekhistorie.
- Admin-configuratie voor zowel `Zaak` als `SearchQuery`.

## Starten

1. Maak een virtuele omgeving en installeer dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Voer migraties uit:
   ```bash
   python manage.py migrate
   ```
3. Maak een admin user:
   ```bash
   python manage.py createsuperuser
   ```
4. Start de server:
   ```bash
   python manage.py runserver
   ```

## Tests

```bash
python manage.py test
```
