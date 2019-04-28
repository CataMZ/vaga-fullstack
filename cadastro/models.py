from django.db import models

class Pokemon(models.Model):
    row = models.PositiveIntegerField()
    name = models.CharField(max_length=40)
    pokedex_number = models.PositiveIntegerField(verbose_name="Pokedex Number")
    img_name = models.PositiveIntegerField()
    generation = models.PositiveIntegerField()
    evolution_stage = models.PositiveIntegerField(verbose_name="Evolution Stage")
    evolved = models.PositiveIntegerField()
    family_id = models.PositiveIntegerField(verbose_name="Family ID")
    cross_gen = models.PositiveIntegerField(verbose_name="Cross Gen")
    type1 = models.CharField(max_length=40, verbose_name="Type 1")
    type2 = models.CharField(max_length=40, verbose_name="Type 2")
    weather1 = models.CharField(max_length=40, verbose_name="Weather 1")
    weather2 = models.CharField(max_length=40, verbose_name="Weather 2")
    stat_total = models.PositiveIntegerField(verbose_name="STAT TOTAL")
    atk = models.PositiveIntegerField(verbose_name="ATK")
    deff = models.PositiveIntegerField(verbose_name="DEF")
    sta = models.PositiveIntegerField(verbose_name="STA")
    legendary = models.PositiveIntegerField()
    aquireable = models.PositiveIntegerField()
    spawns = models.PositiveIntegerField()
    regional = models.PositiveIntegerField()
    raidable = models.PositiveIntegerField()
    hatchable = models.PositiveIntegerField()
    shiny = models.PositiveIntegerField()
    nest = models.PositiveIntegerField()
    new = models.PositiveIntegerField()
    future_evolve = models.PositiveIntegerField(verbose_name="Future Evolve")

    def __str__(self):
        return self.name
