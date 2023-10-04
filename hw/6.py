def analyzer(getallenlijst):
    print("gesorteerde list van ints: ", sorted(getallenlijst))
    print('kleinste getal: ', min(getallenlijst), 'en grootste getal: ', max(getallenlijst))
    print('aantal getallen: ', len(getallenlijst), 'en som van de getallen: ', sum(getallenlijst))
    print('gemiddelde: ', sum(getallenlijst) / len(getallenlijst))
    return


gt = "5-9-7-1-7-8-3-2-4-8-7-9"
lijst = list(gt.replace('-', ""))
tlijst = [eval(i) for i in lijst]
analyzer(tlijst)




lijst = list(gt.replace('-', ""))


