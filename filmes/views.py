from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.messages import constants


from .models import Filmes
# Create your views here.

def filmes(request):
    if request.method == 'GET':
        filmes = Filmes.objects.all()
        return render(request, 'filmes.html', {'filmes': filmes})
    elif request.method == 'POST':
        nomeFilmes = request.POST.get('nome_filme')
        assistir = request.POST.get('onde_assistir')
        generoFilme = request.POST.get('genero')
        dataAssistir = request.POST.get('data_assisti')
        diretor = request.POST.get('diretor')
        roteiro = request.POST.get('roteiristas')
        anoLancamento = request.POST.get('ano_lancamento')
        avaliacao = request.POST.get('avaliacao')


        #validacoes
        if (len(nomeFilmes.strip()) == 0 or len(assistir.strip()) == 0 or 
        len(generoFilme.strip()) == 0 or len(dataAssistir.strip()) == 0 or 
        len(diretor.strip()) == 0 or len(roteiro.strip()) == 0 or len(anoLancamento.strip()) == 0 or
        len(avaliacao.strip()) == 0): 
             messages.add_message(request, constants.ERROR, 'Preencha todos os campos, todos sao obrigatorios')
             return redirect('/')

        # os verdes e da classe Filmes do models e os roxos sao as variaveis
        filmes = Filmes(nome_do_filme=nomeFilmes,
                        onde_assisti=assistir,
                        genero_filme=generoFilme,
                        data_assisti=dataAssistir,
                        diretor=diretor,
                        roteirista=roteiro,
                        ano_lancamento_filme=anoLancamento,
                        avaliacao=avaliacao)
        
        filmes.save()
        messages.add_message(request, constants.SUCCESS, 'Filme Adicionado com Sucesso')

        return redirect('/')

# ----------------------------- Editar filme -----------------------------

def editar_filme(request, id):
    filmes = Filmes.objects.get(id=id)
    return render(request, 'update.html', {'filmes': filmes})


def alterar_filme(request, id):
    filmes = Filmes.objects.get(id=id)

    if request.method == 'POST':
        #editando o nome do filme
        editarNomeFilmes = request.POST.get('nome_filme')
        filmes.nome_do_filme = editarNomeFilmes

        #editando o onde assistir
        editarAssistir = request.POST.get('onde_assistir')
        filmes.onde_assisti = editarAssistir

        #editando o genero
        # editarGeneroFilme = request.POST.get('genero')    
        # filmes.genero_filme = editarGeneroFilme

        #editando o data assistir
        editarDataAssistir = request.POST.get('data_assisti')
        filmes.data_assisti = editarDataAssistir

        #editando o diretor do filme
        editarDiretor = request.POST.get('diretor')
        filmes.diretor = editarDiretor

        #editando o roteiro
        editarRoteiro = request.POST.get('roteiristas')
        filmes.roteirista = editarRoteiro

        #editando o ano de lançamento do filme
        editarAnoLancamento = request.POST.get('ano_lancamento')
        filmes.ano_lancamento_filme = editarAnoLancamento

        #editando a avaliaçao do filme
        editarAvaliacao = request.POST.get('avaliacao')
        filmes.avaliacao = editarAvaliacao

        #validacoes ???
            # if (len(nomeFilmes.strip()) == 0 or len(assistir.strip()) == 0 or 
            # len(generoFilme.strip()) == 0 or len(dataAssistir.strip()) == 0 or 
            # len(diretor.strip()) == 0 or len(roteiro.strip()) == 0 or len(anoLancamento.strip()) == 0 or
            # len(avaliacao.strip()) == 0): 
            #      messages.add_message(request, constants.ERROR, 'Preencha todos os campos, todos sao obrigatorios')
            #      return redirect('/')


        filmes.save()
        return redirect ('/')
    
    return render (request, 'filmes.html', {'filmes': filmes})


# -------------------------------- deletar ---------------------------------
def deletar_filme(request,id):
    filmes = Filmes.objects.get(id=id)

    if request.method == 'POST':
        filmes.delete()
        return redirect('/')
    
    return render(request, 'deletar.html', {'filmes': filmes})

# ---------------------------------------------------------------------------

def indicados(request):
    return render(request, 'indicados.html')

def melhores2020(request):
    return render(request, 'melhores2020.html')

def melhores2021(request):
    return render(request, 'melhores2021.html')




