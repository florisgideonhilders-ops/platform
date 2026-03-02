from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Zaak',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('octopus_zaaknummer', models.CharField(max_length=100, unique=True)),
                ('onderwerp', models.CharField(blank=True, max_length=200)),
                ('dictum', models.CharField(blank=True, max_length=200)),
                ('advies_tekst', models.TextField()),
                ('aangemaakt_op', models.DateTimeField(auto_now_add=True)),
            ],
            options={'ordering': ['-aangemaakt_op']},
        ),
        migrations.CreateModel(
            name='SearchQuery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zoekterm', models.CharField(max_length=200)),
                ('onderwerp_filter', models.CharField(blank=True, max_length=200)),
                ('dictum_filter', models.CharField(blank=True, max_length=200)),
                ('resultaten_telling', models.PositiveIntegerField(default=0)),
                ('aangemaakt_op', models.DateTimeField(auto_now_add=True)),
                ('gebruiker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={'ordering': ['-aangemaakt_op']},
        ),
    ]
