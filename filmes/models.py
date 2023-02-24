from django.db import models

from multiselectfield import MultiSelectField
# Create your models here.

class Filmes(models.Model):
    choices_onde_assisti = (
        ('Prime Video','Prime Video'),
        ('Netflix','Netflix'),
        ('Sony/Marvel','Sony/Marvel'),
        ('HBO Max','HBO Max'),
        ('Marvel','Marvel'),
        ('Star+','Star+'),
        ('DC','DC'),
        ('Fox','Fox'),
        ('Cinema','Cinema'),
        ('Não Oficial','Não Oficial'),
    )

    choices_genero_filme = (
        ('Ação','Ação'),
        ('Ficção Cientifica','Ficção Cientifica'),
        ('Heroi','Heroi'),
        ('Aventura','Aventura'),
        ('Fantasia','Fantasia'),
        ('Velho Oeste','Velho Oeste'),
        ('Drama','Drama'),
        ('Thriller','Thriller'),
        ('Horror','Horror'),
        ('Esportes','Esportes'),
        ('Comedia','Comedia'),
        ('Animação','Animação'),
        ('Guerra','Guerra'),
        ('Misterio','Misterio'),
        ('Crime','Crime'),
        ('Musical','Musical'),
        ('Terror','Terror'),
        ('Romance','Romance'),
        ('Suspence', 'Suspence'),
        ('Cinebiografia','Cinebiografia'),
    )
    choices_avaliacao_filme = (
        ('Muito Ruim', 'Muito Ruim'),
        ('Ruim', 'Ruim'),
        ('Okay', 'Okay'),
        ('Bom', 'Bom'),
        ('Otimo', 'Otimo'),
        ('Excelente', 'Excelente'),
    )

    #editar o tamanho maximo do genero para maior

    nome_do_filme = models.CharField(max_length=100)
    onde_assisti = models.CharField(max_length=120, choices=choices_onde_assisti)
    genero_filme = MultiSelectField(max_length=120, choices=choices_genero_filme)
    data_assisti = models.DateField(null=False, blank=False)
    diretor = models.CharField(max_length=100)
    roteirista = models.CharField(max_length=100)

    # ver depois se tem como pega somente o ano, sem ser por integer field
    ano_lancamento_filme = models.IntegerField()
    #ser como vai ser a avaliaçao vai ser assim
    avaliacao = models.CharField(max_length=20, choices=choices_avaliacao_filme)

    def __str__(self):
        return self.nome_do_filme
    


