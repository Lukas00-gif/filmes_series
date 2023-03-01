from django.shortcuts import render
from django.shortcuts import redirect
from datetime import datetime
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.messages import constants

from series.models import Series

# Create your views here.

def pag_series(request):
    if request.method == 'GET':
        series = Series.objects.all()
        return render(request, 'series.html', {'series': series})
    
    elif request.method == 'POST':
        #estou pegando/atribuindo a variavel nova ao name do html
        nomeSerie = request.POST.get('nome_da_serie')
        temporadaSerie = request.POST.get('temporada_serie')
        episodioSerie = request.POST.get('episodio_serie')
        streamingSerie = request.POST.get('streaming_serie')
        dataSerie = request.POST.get('data_serie')
        statusSerie = request.POST.get('status_serie')

        #validaçoes
        if (len(nomeSerie.strip()) == 0): 
            messages.add_message(request, constants.ERROR, 'Coloque o Nome do Filme')
            return redirect('series')
        
        # o isdigit() e um metodo para falar que so pode numeros, so da um not para 
        #para nao ter numeros
        if not temporadaSerie.isdigit() or not episodioSerie.isdigit():
            messages.add_message(request, constants.WARNING, 'A temporada ou Episodio so Podem ser Numeros')
            return redirect('series')
        
        #fazer um tratamento de data_atual > data_de_verificaçao, para a data nao ser menor 
        #com a data atual, mais tem que att o model para data que irei assistir
        if not dataSerie:
            messages.add_message(request, constants.WARNING, 'Precisa Preencher a Data, Data Invalida')
            return redirect('series')

        # agora e ligando o models da Serie com as variaveis
        series = Series(nome_serie=nomeSerie,
                        temporada=temporadaSerie,
                        episodio=episodioSerie,
                        streaming=streamingSerie,
                        data_assistir_serie=dataSerie,
                        status=statusSerie
                        )
        
        series.save()
        messages.add_message(request, constants.SUCCESS, 'Serie Adicionado com Sucesso')

        return redirect('series')
    

# ------------------------------ editar series ------------------------------



