from django.shortcuts import render
from cadastro.forms import CadPokemon

def cadastrar_pokemons(request):
    formulario = CadPokemon(request.POST or None)

    if formulario.is_valid():
        formulario.save()
        formulario = CadPokemon()

    context = {
        'form': formulario
    }

    return render(request, 'index.html', context)
