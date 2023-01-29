
import matplotlib.pyplot as plt
import json, random
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
print(current_dir)
os.chdir(current_dir)

f = open('rygskv2.json')

popu = int(input("How big is the population (x >= 20)? "))
generations = int(input("How many generations? "))


data = json.load(f)
f.close()

class Individual:
    def __init__(self, gen):
        self.items = []
        self.fit = 0
        self.weight = 0
        self.round = gen

    def assign(self,dad, mom):
        for i in dad.items:
            self.items.append(i)
        for i in mom.items:
            self.items.append(i)
        self.items = [dict(t) for t in {tuple(d.items()) for d in self.items}]
        for i in range(0, len(self.items)):
            num = random.randrange(0, 9)
            if num > 3 and num < 5:
                self.items.pop(random.randrange(len(self.items)))
            elif num > 6:
                self.items.append(data[random.randrange(len(data))])
        self.items = [dict(t) for t in {tuple(d.items()) for d in self.items}]

    def addItem(self,itm):
        self.items.append(itm)

    def fitness(self):
        for i in self.items:
            self.fit += int(i["price"])
            self.weight += int(i["weight"])
        if self.weight > 5000:
            self.fit = 0


pop_list = []
tot_fit = 0
for x in range(popu):
    p1 = Individual(0)
    for z in range(3):
        p1.addItem(data[random.randrange(len(data))])
    p1.fitness()
    tot_fit += p1.fit
    pop_list.append(p1)
fittest = pop_list[0]
fit_list = []


for _gen in range(generations):
    
    newlist = sorted(pop_list, key=lambda d: d.fit,reverse=True)
    #print(newlist[0].items)
    pop_list.clear()
    for z in range(round(popu/10)-1):
        pop_list.append(newlist[z])
        for _ in range(round(popu/30)):
            p1 = Individual(_gen)
            p1.assign(newlist[z], newlist[round(popu/10)-1-z])
            p1.fitness()
            pop_list.append(p1)
    fit_list.append(newlist[0].fit)
    if fittest == newlist[0]:
        pass
    else: 
        fittest = newlist[0]
    newlist.clear()

print(f"\n\tFittest Backpack:\nTotal Cost: {fittest.fit}, Total Weight: {fittest.weight}, at round {fittest.round}")
#print(fittest.items)
#[print(i["item"],i["price"]) for i in fittest.items ]
#print("List of Fit-value per generation",fit_list)
plt.plot([i for i in range(1,len(fit_list)+1)],fit_list)
plt.xlabel("Generations")
plt.ylabel("Fittest Backpack Value")
plt.show()

