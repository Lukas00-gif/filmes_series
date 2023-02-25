from django.db import models

# Create your models here.

class Series(models.Model):
    #pelo jeito tem q modificar os choices para ficarem iguais
    streamings_choices = (
        ('prime_video','Prime Video'),
        ('netflix','Netflix'),
        ('hbo_max','HBO Max'),
        ('disney+','Disney+'),
        ('star+','Star+'),
        ('fox','Fox'),
        ('paramout+','Paramout+'),
        ('amc','AMC'),
        ('não_oficial','Não Oficial'),
    )
    status_choices = (
        #primeiro e o q vai ficar akii no models | segundo vai aparecer
        ('em_breve', 'Em Breve'),
        ('assistindo', 'Assistindo'),
        ('pausado', 'Pausado'),
        ('finalizada','Finalizada'),
        ('cancelado', 'Cancelado'),
    )

    #colocar algo sobre o seasion finale e series finale dps
    nome_serie = models.CharField(max_length=120)
    temporada = models.IntegerField()
    episodio = models.IntegerField()
    streaming = models.CharField(max_length=50, choices=streamings_choices)
    data_assistir_serie = models.DateField()
    status = models.CharField(max_length=50, choices=status_choices)
    
    def __str__(self):
        return self.nome_serie

