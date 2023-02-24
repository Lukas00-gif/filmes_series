# Generated by Django 4.1.4 on 2023-01-12 16:44

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('filmes', '0002_alter_filmes_genero_filme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filmes',
            name='genero_filme',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Ação', 'Ação'), ('Ficção Cientifica', 'Ficção Cientifica'), ('Heroi', 'Heroi'), ('Aventura', 'Aventura'), ('Fantasia', 'Fantasia'), ('Velho Oeste', 'Velho Oeste'), ('Drama', 'Drama'), ('Thriller', 'Thriller'), ('Horror', 'Horror'), ('Esportes', 'Esportes'), ('Comedia', 'Comedia'), ('Animação', 'Animação'), ('Guerra', 'Guerra'), ('Misterio', 'Misterio'), ('Crime', 'Crime'), ('Musical', 'Musical'), ('Terror', 'Terror'), ('Romance', 'Romance'), ('Suspence', 'Suspence'), ('Cinebiografia', 'Cinebiografia')], max_length=20),
        ),
    ]
