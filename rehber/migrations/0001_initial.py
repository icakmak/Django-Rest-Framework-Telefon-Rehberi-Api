# Generated by Django 3.2.9 on 2021-11-13 12:14

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
            name='Profil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sehir', models.CharField(blank=True, max_length=100)),
                ('kendiNo', models.CharField(blank=True, max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profil', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Profiller',
            },
        ),
        migrations.CreateModel(
            name='Rehber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isimsoyisim', models.CharField(max_length=150)),
                ('telno', models.CharField(max_length=20)),
                ('yaratilma_zamani', models.DateTimeField(auto_now_add=True)),
                ('guncelleme_zamani', models.DateTimeField(auto_now=True)),
                ('user_profil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rehber.profil')),
            ],
            options={
                'verbose_name_plural': 'Numaralar',
            },
        ),
    ]
