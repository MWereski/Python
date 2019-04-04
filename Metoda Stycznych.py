import copy

print("Metoda Stycznych")

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
            while(len(wiel2) - i > a and wiel2[i+a].isdigit()):
                x = x+wiel2[i+a]
                flaga+=1
                a+=1
            tab.append(int(x))
            #if(i == len(wiel2)-1):
             #   for q in range(0, int(x)):
              #      tab.append(int(0))
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

if(tab[len(tab)-1] != 0):
    for z in range(0, tab[len(tab)-1]):
        tab.append(0);

print("Pierwsza pochodna")
tablica_p = copy.deepcopy(tablica)
tab_p = copy.deepcopy(tab)

print(tablica_p)
print(tab_p)

for z in range(0, len(tablica_p)):
    tablica_p[z] = tablica_p[z] * tab[z]
    if(tab_p[z] - 1 < 0):
        tab_p[z] = 0;
    else:
        tab_p[z] -= 1;

wynik = ""
p = 0
for x in range(0, len(tablica_p)):
    if(tablica_p[p] == 0):
        p+=1
        continue
    if(tablica_p[p]==1 and p == 0):
        if(tab[p]-1 == 1):
            wynik += "x"
        elif(tab[p]-1 == 0):
            wynik += str(1)
        else:
            wynik += "x^" + str(tab[p]-1)
    elif(tablica_p[p]==-1 and p == 0):
        if(tab[p]-1 == 1):
            wynik += "-x"
        elif(tab[p]-1 == 0):
            wynik += str(-1)
        else:
            wynik += "x^" + str(tab[p]-1)
    elif(tablica_p[p]==1):
        if(tab[p]-1 == 1):
            wynik += "+x"
        elif(tab[p]-1 == 0):
            wynik += "+1"
        else:
            wynik += "+x^" + str(tab[p]-1)
    elif(tablica_p[p]==-1):
        if(tab[p]-1 == 1):
            wynik += "-x"
        elif(tab[p]-1 == 0):
            wynik += str(-1)
        else:
            wynik += "-x^" + str(tab[p]-1)
    elif(tablica_p[p] > 0):
        if(tab[p]-1 == 1):
            wynik += "+" + str(tablica_p[p]) + "x"
        elif(tab[p]-1 == 0):
            wynik += "+" + str(tablica_p[p])
        else:
            wynik += "+" + str(tablica_p[p]) + "x^" + str(tab[p]-1)
    elif(tablica_p[p] < 0):
        if(tab[p]-1 == 1):
            wynik += str(tablica_p[p]) + "x"
        elif(tab[p]-1 == 0):
            wynik +=str(tablica_p[p])
        else:
            wynik += str(tablica_p[p]) + "x^" + str(tab[p]-1)
    else:
        wynik += str(tablica_p[p]) + "x^" + str(tab[p]-1)
    p+=1
print("Pochodna : " + str(wynik))

def wartosc(t, p, zmienna):
    w = 0
    
    for z in range(0, len(t)):
        w += t[z] * (zmienna**p[z])
    
    return w

print("Podaj dokładnośc do jakiej chcesz otrzymać wynik")
d = float(input());
print("Podaj przedział : od ")
p1 = int(input())
print("do ")
p2 = int(input())
if(p1 > p2):
    q = p1
    p1 = p2
    p2 = q
print("Przedział : [ " + str(p1) + ", " + str(p2) + " ]")

x0 = p2;
m = wartosc(tablica_p, tab_p, p1)
while(True):
    
    xn = x0 - wartosc(tablica, tab, x0)/wartosc(tablica_p, tab_p, x0)

    if(abs(xn - x0) <= d):
        print("Końcowy wynik : " + str(xn))
        break
    else:
        x0 = xn
        
    
