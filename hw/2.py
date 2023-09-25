import time

print(0 == (1 == 2))
print(2 + (3 == 4) + 5 == 7)
print((1 < -1) == (3 > 4))


per_uur = input("wat verdien je per uur ")
uur = input('hoeveel uur heb je gewerkt ')
betaald = float(per_uur) * int(uur)
time.sleep(2)
print(str(uur), 'uur werken levert ', str(betaald), 'op')
