
print("Witaj w Hornerze ")
print("Działa dla liczb całkowitych i ułamków")
wielomian = input("Podaj Wielomian (np.: 3x^2 + 4x - 3): ")
i = 0
liczba = 0
flaga = 0
tablica = []
tab = []
ile_x = 0
wiel2 = ""
flaga_dziel = 0
for x in wielomian:
    if(x != " "):
        wiel2 += x
for x in wiel2:
    a = 1
    if(x == "/"):
        flaga_dziel = 1
    if(i < len(wiel2)-2 and x == "x" and wiel2[i+1] != "^"):
        tab.append(int(1))
    if(x == "x" and i == len(wiel2)-1):
        tab.append(int(1))
    if(flaga!= 0):
        flaga -=1
        i+=1
        continue
    if(x.isdigit()):
        if(i > 0 and not wiel2[i-1] == "^"):
            if(wiel2[i-1] == "-"):
                while(len(wiel2) - i > a and wiel2[i+a].isdigit()):
                    x = x+wiel2[i+a]
                    flaga+=1
                    a+=1
                if(flaga_dziel == 1):
                    tablica[len(tablica)-1] = ((float(tablica[len(tablica)-1])/int(x)) * -1)
                    flaga_dziel = 0
                else:
                    tablica.append(int(x) * -1)
                i +=1
                continue
            while(len(wiel2) - i > a and wiel2[i+a].isdigit()):
                x = x+wiel2[i+a]
                flaga+=1
                a+=1
            if(flaga_dziel == 1):
                tablica[len(tablica)-1] = (float(tablica[len(tablica)-1])/int(x))
                flaga_dziel = 0
            else:
                tablica.append(int(x))
        elif(i > 0 and wiel2[i-1] == "^"):
            while(wiel2[i+a].isdigit()):
                x = x+wiel2[i+a]
                flaga+=1
                a+=1
            tab.append(int(x))
            if(i == len(wiel2)-1):
                for q in range(0, int(x)):
                    tab.append(int(0))
        elif(i == 0):
            while(wiel2[i+a].isdigit()):
                x = x+wiel2[i+a]
                flaga+=1
                a+=1
            if(flaga_dziel == 1):
                tablica[len(tablica)-1] = (float(tablica[len(tablica)-1])/int(x))
                flaga_dziel = 0
            else:
                tablica.append(int(x))
    elif(i>0 and x=="x" and not wiel2[i-1].isdigit()):
        if(wiel2[i-1] == "-"):
            tablica.append(int(1)* -1)
        else:
            tablica.append(int(1))
    elif(i == 0 and x == "x"):
        tablica.append(int(1))
    if(x == "x" and i == len(wiel2)-1):
        tablica.append(0)
        
    i +=1
dziel = input("Podaj teraz dwumian(np.: x - 1) : ")
b = 1
j = 0
dziel2 = ""
flaga_dziel = 0
licze = 1
for x in dziel:
    if(x != " "):
        dziel2 += x
for x in dziel2:
    if x == "/":
        flaga_dziel=1
    if x.isdigit():
        if(flaga_dziel != 1):
            while(len(dziel2) - j > b and dziel2[j+b].isdigit()):
                x = x+dziel2[j+b]
                b+=1
            if(dziel2[j-1] == "-"):
                liczba = int(x)
            else:
                liczba = int(x)* -1
        else:
            while(len(dziel2) - j > b and dziel2[j+b].isdigit()):
                 x = x+dziel2[j+b]
                 b+=1
            if(dziel2[j-1] == "-"):
                licze = int(x) * -1
            else:
                licze = int(x)
            liczba = float(liczba / licze)
    j+=1

p = 0
z = tab[0]
while(p < len(tab)):
     if(tab[p] != z):
         for l in range(1,z - tab[p]):
            tab.insert(p, 0)
            p+=1
     elif(tab[p] == z):
         p+=1
         if(p == len(tab)-1 and tab[p] == 0):
             break
         continue
     z=tab[p]

if(tab[len(tab)-1] >= 1):
    for l in range(1,tab[p-1]+1):
        tab.append(0)
p = 0
while(p < len(tab)-1):
    if(tab[p] == 0):
        tablica.insert(p, 0)
    p+=1
p = 0
for x in range(tab[0], 0, -1):
    tab[p] = x
    p+=1
    
print("======= OBLICZANIE ===== -_-")

p = 1
for x in range(0, len(tablica)-1):
    tablica[p] = (tablica[p-1] * liczba)+ tablica[p]
    p+=1
wynik = ""
p = 0
for x in range(0, len(tablica)-1):
    if(tablica[p] == 0):
        p+=1
        continue
    if(tablica[p]==1 and p == 0):
        if(tab[p]-1 == 1):
            wynik += "x"
        elif(tab[p]-1 == 0):
            wynik += str(1)
        else:
            wynik += "x^" + str(tab[p]-1)
    elif(tablica[p]==-1 and p == 0):
        if(tab[p]-1 == 1):
            wynik += "-x"
        elif(tab[p]-1 == 0):
            wynik += str(-1)
        else:
            wynik += "x^" + str(tab[p]-1)
    elif(tablica[p]==1):
        if(tab[p]-1 == 1):
            wynik += "+x"
        elif(tab[p]-1 == 0):
            wynik += "+1"
        else:
            wynik += "+x^" + str(tab[p]-1)
    elif(tablica[p]==-1):
        if(tab[p]-1 == 1):
            wynik += "-x"
        elif(tab[p]-1 == 0):
            wynik += str(-1)
        else:
            wynik += "-x^" + str(tab[p]-1)
    elif(tablica[p] > 0):
        if(tab[p]-1 == 1):
            wynik += "+" + str(tablica[p]) + "x"
        elif(tab[p]-1 == 0):
            wynik += "+" + str(tablica[p])
        else:
            wynik += "+" + str(tablica[p]) + "x^" + str(tab[p]-1)
    elif(tablica[p] < 0):
        if(tab[p]-1 == 1):
            wynik += str(tablica[p]) + "x"
        elif(tab[p]-1 == 0):
            wynik +=str(tablica[p])
        else:
            wynik += str(tablica[p]) + "x^" + str(tab[p]-1)
    else:
        wynik += str(tablica[p]) + "x^" + str(tab[p]-1)
    p+=1
print("wynik = " + str(wynik) + " reszta = " + str(tablica[len(tablica)-1]))
