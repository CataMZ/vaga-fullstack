from django.db import models

class Pokemon(models.Model):
    row = models.PositiveIntegerField()
    name = models.CharField(max_length=40)
    pokedex_number = models.PositiveIntegerField()
    img_name = models.PositiveIntegerField()
    generation = models.PositiveIntegerField()
    evolution_stage = models.PositiveIntegerField()
    evolved = models.PositiveIntegerField()
    family_id = models.PositiveIntegerField()
    cross_gen = models.PositiveIntegerField()
    type1 = models.CharField(max_length=40)
    type2 = models.CharField(max_length=40)
    weather1 = models.CharField(max_length=40)
    weather2 = models.CharField(max_length=40)
    stat_total = models.PositiveIntegerField()
    atk = models.PositiveIntegerField()
    deff = models.PositiveIntegerField()
    sta = models.PositiveIntegerField()
    legendary = models.PositiveIntegerField()
    aquireable = models.PositiveIntegerField()
    spawns = models.PositiveIntegerField()
    regional = models.PositiveIntegerField()
    raidable = models.PositiveIntegerField()
    hatchable = models.PositiveIntegerField()
    shiny = models.PositiveIntegerField()
    nest = models.PositiveIntegerField()
    new = models.PositiveIntegerField()
    future_evolve = models.PositiveIntegerField()   

    def __str__(self):
        return self.name
