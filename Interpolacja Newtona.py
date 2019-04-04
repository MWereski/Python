import copy;



def dodawanie_punktow():
    
    while(1):
        flaga = False
        print("Podaj x");
        x[0] = int(input());
        for z in punkty:
            if(x[0] == z[0]):
                print("Istnieje taki punkt")
                flaga = True
        if(flaga == True):
            continue;
        print("Podaj y");
        x[1] = int(input());
        punkty.append(copy.deepcopy(x));
        print("Czy chcesz obliczyć? t/n");
        z = input();
        if(z == "t"):
            break;
def obliczenia():
    
    i = 0;
    w = 1;
    e = 1;
    r = 1;

    for z in punkty:
        kolumna.append(z[1]);
    piramida.append(copy.deepcopy(kolumna));

    while(i < len(piramida[0])-1):
        kolumna.clear();
        e = 1;
        for z in range(0, len(piramida[i])-1):
        
            q = (piramida[w-1][e] - piramida[w-1][e-1]) / (punkty[e+i][0] - punkty[e-r+i][0]);
            kolumna.append(q);
            e+=1;
        piramida.append(copy.deepcopy(kolumna));
        w+=1;
        i+=1;
        r+=1;

def wyniki():
    wynik = ""
    ile = 0
    for z in piramida:
        iksy = 0
        if(z[0] == 0):
           continue
        if(z[0] < 0):
            if(z[0] == -1 and ile == 0):
                wynik +=  str(z[0])
            elif(z[0] == -1):
                wynik += " - "
            else:
                wynik += " " + str(z[0])
        else:
            if(ile == 0):
                wynik += str(z[0])
            elif(z[0] == 1):
                wynik += " + "
            else:
                wynik += " + " + str(z[0])
        for c in range(0, ile):
            if(punkty[iksy][0] > 0):
                wynik += "(x - "+str(punkty[iksy][0])+")"
            else:
                wynik += "(x + "+str(punkty[iksy][0]*-1)+")"
            iksy += 1
            if(iksy >= len(punkty)):
                break;
        ile += 1
    
    return wynik;

print("INTERPOLACJ1A NEWTONA");
x = [0 ,0];
punkty = [];
piramida = [];
kolumna = [];

dodawanie_punktow();
obliczenia();

print("Podane punkty:");
print(punkty)
print("Wynik : "+wyniki())

print("Czy chcesz dodać punkt? t/n")
k = input();
while(k == "t"):
    piramida = [];
    kolumna = [];
    
    dodawanie_punktow();
    obliczenia();
    print("Podane punkty:");
    print(punkty);
    print("Wynik : "+wyniki())
    
    print("Czy chcesz dodać punkt? t/n")
    k = input();
print(piramida)
print("Koniec")
