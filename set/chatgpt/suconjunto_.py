#Verifique se o conjunto {1, 2, 3} é subconjunto de {0, 1, 2, 3, 4, 5}.
conjunto1 = {1, 2, 3}
conjunto2 = {0, 1, 2, 3, 4, 5}
subconjunto = conjunto1 & conjunto2
if subconjunto == conjunto1:
    subconjunto = True
print(subconjunto)


