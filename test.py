fil = open('data/data.txt', 'r')
indhold = fil.read()
print(indhold)
fil.close()

strings = indhold.split(" ")
for i in strings:
    print(i)

class Ting:
    name = ""
    weight = 0
    value = 0


