# Generated by Django 4.1.4 on 2023-01-11 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filmes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_do_filme', models.CharField(max_length=100)),
                ('onde_assisti', models.CharField(choices=[('Prime Video', 'Prime Video'), ('Netflix', 'Netflix'), ('Sony/Marvel', 'Sony/Marvel'), ('HBO Max', 'HBO Max'), ('Marvel', 'Marvel'), ('Star+', 'Star+'), ('DC', 'DC'), ('Fox', 'Fox'), ('Cinema', 'Cinema'), ('Não Oficial', 'Não Oficial')], max_length=20)),
                ('genero_filme', models.CharField(choices=[('Ação', 'Ação'), ('Ficção Cientifica', 'Ficção Cientifica'), ('Heroi', 'Heroi'), ('Aventura', 'Aventura'), ('Fantasia', 'Fantasia'), ('Velho Oeste', 'Velho Oeste'), ('Drama', 'Drama'), ('Thriller', 'Thriller'), ('Horror', 'Horror'), ('Esportes', 'Esportes'), ('Comedia', 'Comedia'), ('Animação', 'Animação'), ('Guerra', 'Guerra'), ('Misterio', 'Misterio'), ('Crime', 'Crime'), ('Musical', 'Musical'), ('Terror', 'Terror'), ('Romance', 'Romance'), ('Cinebiografia', 'Cinebiografia')], max_length=20)),
                ('data_assisti', models.DateField()),
                ('diretor', models.CharField(max_length=100)),
                ('roteirista', models.CharField(max_length=100)),
                ('ano_lancamento_filme', models.IntegerField()),
                ('avaliacao', models.CharField(choices=[('Muito Ruim', 'Muito Ruim'), ('Ruim', 'Ruim'), ('Okay', 'Okay'), ('Bom', 'Bom'), ('Otimo', 'Otimo'), ('Excelente', 'Excelente')], max_length=20)),
            ],
        ),
    ]
