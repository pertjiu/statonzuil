import random
# infile = open("kluisgegeven.txt", "r")
# content = infile.read()
# textcontent = content.split('\n')
# infile.close()

kluizen  = [i for i in range(1, 13)]
print(kluizen)
with open('kluisgegeven.txt', 'r') as file:
   # content = file.readlines()
    for line in file:
        kluis = int(line.strip().split(';')[0])
        if kluis in kluizen:
            kluizen.remove(kluis)
#print(kluizen)
if kluizen:
    beschikbaar = kluizen[0]
    print(beschikbaar)
else:
    ''''return'''''
    print(-2)


ww = input('wachtword van minimaal 4 tekens ')
if len(ww) < 4 or ";" in ww:
    ''''return'''
    print(-1)
file.close()

with open('kluisgegeven.txt', 'a') as file:
    gegevens = f'{beschikbaar};{ww}' + '\n'
    file.write(gegevens)






















