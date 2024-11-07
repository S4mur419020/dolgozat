import random
import math


def feladat1():
    szam:int=int(input(print("Adj meg egy páros számot: ")))
    while (szam%2!=0):
        szam:int=int(input(print("Adj meg egy páros számot: ")))
    print(szam)
    
def feladat2():
    lista=[]
    i=0
    while i<13:
        rszam:int=int(random.random()*(141)+10)
        lista.append(rszam)
        i+=1
    return lista

def feladat2_2(lista):
    i:int=0
    db:int=0
    while(i<len(lista)):
        if(lista[i]%3==0):
            db+=1
        i+=1
        
    return db

def feladat3(szov, N):
    i:int=0
    hossz:int=0
    if N>len(szov):
        print("Nincs N. karakter!")
    else:
        print(szov[N-1].upper()*3)
        


def feladat4():
    szov= []
    s=szov

    szoveg:str=""
    while szoveg !="@":
        szoveg=input("Adj nevet!(kilépés @ jellel: ")
        szov.append(szoveg)
        if szoveg!="@":
            print(szoveg)
    print(f"A felhasználó {szov} nevet adott meg")