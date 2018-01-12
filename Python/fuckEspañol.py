from random import randint

fuck = 'fuck '
palabro = ''
fuckpalabro = ''
palabras = []

def palabraRandom():
        with open('palabrasEsp.txt', 'r', encoding='utf-8') as file:
                for palabra in file:
                        palabras.append(palabra)
        file.close()
        numeroRandom = randint(0, len(palabras)-1)
        return palabras[numeroRandom]


palabro = palabraRandom().replace("\n", "")
fuckpalabro = (fuckpalabro.join([fuck,palabro]))


print (fuckpalabro)
