import math

def znajdz(a):
    liczba = a
    wynik = 0
    while liczba > 0:
        reszta = liczba % 10
        wynik = wynik * 10 + reszta
        liczba = math.floor(liczba / 10)
    return wynik

def lustro(a,b):
    liczba =a
    for j in range(b):
        odwrot=znajdz(liczba)
        liczba=liczba+odwrot
        liczba_stringowa=str(liczba)
        palindrom=True
        for i in range(math.floor(len(liczba_stringowa)/2)):
            if liczba_stringowa[i]!=liczba_stringowa[len(liczba_stringowa)-1-i]:
                palindrom=False
        if palindrom==True:
            return liczba
    return -1
            
print(lustro(125,3))
print(lustro(91,2))
print(lustro(91,1))
