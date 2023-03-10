print ('Welkom bij Papi Gelato')

hoorntje = 0
bakje = 0
prijshoorntje = 1.25 
prijsbakje = 0.75
prijsbolletjes = 0.95 

slagroom = 0
sprinkels = 0
Caramelsaus = 0

def Topping(HoornOfBak, bolletjes):
    global sprinkels
    global slagroom
    global Caramelsaus
    topping = input ("Wat voor topping wilt u: (A) Geen, (B) Slagroom, (C) Sprinkels of (D) Caramel Saus?")
    while True:
        if topping.lower () == 'a':
            break
        elif topping.lower() == 'b':
            slagroom += 0.50 
            break
        elif topping.lower() == 'c':
            sprinkels += (bolletjes * 0.30)
            break
        elif topping.lower() == 'd':
            if HoornOfBak  == "bakje":
                Caramelsaus += 0.90
            elif HoornOfBak == "hoorntje":
                Caramelsaus +=0.60
            break
        else:
            print ("Sorry dat is geen optie die we aanbieden...")


def Smaken(bolletjes):
    alleSmaken = []
    for bolletje in range(bolletjes):
        while True:
            smaken = input (f"Welke smaak wilt u voor de bolletjes? u heeft {bolletje} (A) Aardbei , (C) Chocolade, (V) Vanille? ")
            if smaken.lower() == 'a':
                alleSmaken.append("Aardbei")
                break
            elif smaken.lower() == 'c':
                alleSmaken.append("Chocolade")
                break
            elif smaken.lower() == 'v':
                alleSmaken.append("Vanille")
                break
            else:
                print ("Sorry dat is geen optie die we aanbieden...")
    return alleSmaken

def meerBestellen():
        bestellen = input ("Wilt u nog meer bestellen? Y/N: ")
        if bestellen == "Y" or bestellen == "y":
            print ("Met genoegen") 
            return True
        elif bestellen == "N" or bestellen == "n":
            print ("Bedankt en tot ziens!")
        else:
            print ("Sorry, Dat snap ik niet")
            return False

        
def AantBolletjes():
    while True:
        bolletjes = int(input ("Hoeveel bolletjes wilt u?: "))
        if bolletjes >= 8 or bolletjes <= 0:
            print("Zulke grote bakken hebben we niet!")
        else:
            return bolletjes
while True:
    PariculierOfZakelijk = int(input("1)Particulier of 2)Zakelijk "))
    if PariculierOfZakelijk != 1 and PariculierOfZakelijk != 2:
        print("Sorry dat snap ik niet!")
    else:
        break

if PariculierOfZakelijk == 1:
    while True:
        bolletjes = AantBolletjes()
        smaken = Smaken(bolletjes) 
        print(smaken)
        if bolletjes <= 3:
            while True:
                onderkant = input (f"Wilt u deze {bolletjes} bolletje(s) in een (A)hoorntje of (B)bakje?: ")
                if onderkant.lower() == 'b':
                    Topping('bakje', bolletjes)
                    bakje += 1
                    print('Bakje')
                    
                    break
                elif onderkant.lower() == 'a': 
                    Topping('hoorntje' , bolletjes)
                    hoorntje += 1
                    print ('Hoorntje')
                    break
                else:
                    print("Sorry, dat snap ik niet...")
        elif bolletjes >= 4 and bolletjes <= 8:
            Topping ('bakje' , bolletjes)
            print (f"Hier is uw {bolletjes} bolletjes")

        if meerBestellen():
            print()
        else:
            berekeningBolletjes = bolletjes * prijsbolletjes
            berekeningHoorntje = hoorntje * prijshoorntje
            berekeningBakje = bakje * prijsbakje
            berekeningToppings = Caramelsaus + slagroom + sprinkels
            berekningAlles = berekeningBolletjes + berekeningHoorntje + berekeningBakje + berekeningToppings

            print ("---------[Papi Gelato]---------")
            print (f"Bolletjes = {berekeningBolletjes}" )
            if hoorntje > 0:   
                print (f"Hoorntje = {berekeningHoorntje}")
            if bakje > 0:
                print(f"Bakje = {berekeningBakje}")
            if berekeningToppings > 0:
                print (f"Toppings = {berekeningToppings}")
            print (f"Totaal =  {berekningAlles}")
            break
else:
    liter = int(input("Hoeveel liter wilt u? "))
    for a in range(liter):
        print("(A) Aardbei , (C) Chocolade, (V) Vanille? ")
        smaak = input(f"Welke smaak wilt u voor liter {a + 1} ")
    berekeningLiter = 9.80 * liter
    BTW = berekeningLiter * 0.06
    print ("---------[Papi Gelato]---------")
    print (f"""Liter = {berekeningLiter}
------------ + 
Totaal = {berekeningLiter} 
BTW (6%) = {BTW}
""")
