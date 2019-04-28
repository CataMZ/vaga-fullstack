from django import forms
from cadastro.models import Pokemon

class CadPokemon(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = ['row', 'name', 'pokedex_number', 'img_name', 'generation', 'evolution_stage', 'evolved', 'family_id', 'cross_gen', 'type1', 'type2', 'weather1', 'weather2', 'stat_total', 'atk', 'deff', 'sta', 'legendary', 'aquireable', 'spawns', 'regional', 'raidable', 'hatchable', 'shiny', 'nest', 'new', 'future_evolve']