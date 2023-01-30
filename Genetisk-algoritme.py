#Vi har været lidt stuck og har derfor fået hjælp af Filip. Derfor er små dele af koden fra ham.
import os, json, random
import matplotlib.pyplot as plot
from colorama import Fore

class rygsæk:
    # Denne class indeholder alle de ting, som rygsækken skal indeholde. Den indeholder også en metode, som beregner fitness og vægt. Fitness er summen af alle priserne på tingene i rygsækken, og vægten er summen af alle vægtene på tingene i rygsækken. Hvis vægten overstiger 5000, så sættes fitness til 0, da det ikke er muligt at bære en rygsæk med en vægt på over 5000.
    def __init__(self, gen):
        self.ting = []
        self.fitness = 0
        self.vaegt = 0
        self.runde = gen

    def tilføj(self, tings):
        self.ting.append(tings)

    #Generer er den funktion der skaber "evulutionen".
    def generer(self, mor, far):
        #Tilføjer ting fra mor og far til rygsækken
        for i in mor.ting:
            self.ting.append(i)
        for i in far.ting:
            self.ting.append(i)
        #Fjerner duplikater
        self.ting = [dict(t) for t in {tuple(d.items()) for d in self.ting}]
        #Laver nogle tilfældige ændringer i rygsækken
        for i in range(0, len(self.ting)):
            r = random.random()
            if r < 0.4:
                #Fjerner et tilfældigt element
                self.ting.pop(random.randrange(len(self.ting)))
            elif r > 0.6:
                #Tilføjer et tilfældigt element
                self.ting.append(indhold[random.randrange(len(indhold))])
        #Fjerner duplikater igenl
        self.ting = [dict(t) for t in {tuple(d.items()) for d in self.ting}]

    def beregn_fitness(self):
        for ting in self.ting:
            self.fitness += int(ting["pris"])
            self.vaegt += int(ting["vaegt"])
        if self.vaegt > 5000:
            self.fitness = 0

def import_json():
    #Vi importere filen rygsæk-info.json, det her kode er bare for at den faktisk gider at loade.
    current_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(current_dir)
    #Vi prøver at loade filen, hvis det ikke lykkes, så printes der en fejlbesked og programmet lukkes.
    try:
        f = open('rygsæk-info.json', 'r')
        indhold = json.load(f)
        f.close()
        return indhold
    except:
        print(Fore.RED + 'Der er sket en fejl med at loade rygsæk-info.json, tjek at filen er i samme mappe som programmet')
        exit()

def start_dialog():
    #her er der nogle variabler som bruges til at bestemme hvor mange individer der skal være i hver generation og hvor mange generationer der skal være
    antalGenerationer = int(input(Fore.GREEN + 'Hvor mange generationer vil du have? ' + Fore.WHITE))
    antalIndividerPerGeneration = int(input(Fore.GREEN + 'Hvor mange individer vil du have i hver generation? '  + Fore.WHITE))
    if antalIndividerPerGeneration <= 20:
        print(Fore.RED + 'Der skal være mindst 20 individer i hver generation')
        while antalIndividerPerGeneration <= 20:
            antalIndividerPerGeneration = int(input(Fore.GREEN + 'Hvor mange individer vil du have i hver generation? ' + Fore.WHITE))
    return antalGenerationer, antalIndividerPerGeneration

#Laver en population og putter radom ting i rygsækken. Samt beregner fitness for denne rygsæk og tilføjer den til populationen.
def generer_population(antalIndividerPerGeneration):
    population = []
    total_fitness = 0
    for x in range(antalIndividerPerGeneration):
        fyldtRygsæk = rygsæk(x)
        for i in range(5):
            ting = random.choice(indhold)
            fyldtRygsæk.tilføj(ting)
        fyldtRygsæk.beregn_fitness()
        total_fitness += fyldtRygsæk.fitness
        population.append(fyldtRygsæk)
    fittest = population[0]
    fit_list = []
    return fittest, fit_list, population

def evolution(population, generationer, fit_list, antalIndividerPerGeneration, fittest):
    for _gen in range(generationer):
        sorteret = sorted(population, key=lambda rygsæk: rygsæk.fitness, reverse=True)
        population.clear()
        #Fjerner de 10% svageste
        for i in range(int(antalIndividerPerGeneration/10)-1):
            population.append(sorteret[i])
        #Laver 10% nye individer
            for _ in range(int(antalIndividerPerGeneration/30)):
                nyRygsæk = rygsæk(_gen)
                nyRygsæk.generer(sorteret[i], sorteret[round(antalIndividerPerGeneration/10)-1-i])
                nyRygsæk.beregn_fitness()
                population.append(nyRygsæk)
        fit_list.append(sorteret[0].fitness)
        if fittest == sorteret[0]:
            pass
        else:
            fittest = sorteret[0]
        sorteret.clear()

def tegn_graf(fittest, fit_list):
    print(f"Total Pris: {fittest.fitness} Total Vægt: {fittest.vaegt} Generation: {fittest.runde}")
    plot.plot([i for i in range(1, len(fit_list)+1)], fit_list)
    plot.xlabel("Generation")
    plot.ylabel("Fitness")
    plot.show()

indhold = import_json()
antalGenerationer, antalIndividerPerGeneration = start_dialog()
fittest, fit_list, population = generer_population(antalIndividerPerGeneration)
evolution(population, antalGenerationer, fit_list, antalIndividerPerGeneration, fittest)
tegn_graf(fittest, fit_list)