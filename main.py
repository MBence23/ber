# Az alkalmazás itt fut

from dolgozo import Dolgozo 

class Ber:
    # Konstruktor
    # Az osztályváltozóknak kezdő értéket adunk
    # Adattagok előkészítése 
    def __init__(self):
        self.filename = "berkft.txt" 
        self.dolgozoLista = []
        
    # fálj beolvasása:
    def olvas_fajl(self):
        fp = open(self.filename, "r", encoding="utf-8")
        lines = fp.readlines()
        fp.close()
        for line in lines :
            line = line.rstrip() #sortörés
            (nev, telepules, cim, szuletes, fizetes) = line.split(":") 
            dolgozo = Dolgozo(nev, telepules, cim, szuletes, fizetes)
            self.dolgozoLista.append(dolgozo) 

    # Szolnokiak
    def szolnoki(self):
        szolnokiLista = []
        for dolgozo in self.dolgozoLista:
            if dolgozo.telepules == "Szolnok":
                print(dolgozo.telepules)
                szolnokiLista.append(dolgozo)
        # for vége
        # legfiatalabb; minimumkiválasztás tétel
        max_szolnoki = szolnokiLista[0]
        for szolnoki in szolnokiLista:
            # print(szolnoki.szuletes)
            if szolnoki.szuletes > max_szolnoki.szuletes:
                max_szolnoki = szolnoki
            
    # Hatvani dolgozók fizetése:
    def hatvani_fizetes(self):
        osszeg = 0
        for dolgozo in self.dolgozoLista:
            if dolgozo.telepules == "Hatvan":
                osszeg = osszeg + int(dolgozo.fizetes)
        print("Hatvaniak fizetése:", osszeg)

    # Új függvény 
    def uj_feladat(self):
        pass


# class Ber vége

ber = Ber()
ber.olvas_fajl()
ber.szolnoki()
ber.hatvani_fizetes()
