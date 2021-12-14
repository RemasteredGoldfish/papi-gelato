def stap1():
    print('Welkom bij Papi Gelato')
    bolletjes = input('Hoeveel bolletjes wilt u? ')
    if bolletjes <= '3':
        print(f'Dan krijgt u van mij {bolletjes} bolletjes')
    elif bolletjes <= '8':
        print(f'Dan krijgt u van mij {bolletjes} bolletjes')
    elif bolletjes > '8':
        print('Sorry, zulke grote bakken hebben we niet')
        stap1()
    return bolletjes
stapje1 = stap1()
def stap2(bolletjes):
    
    houder = input("Wilt u deze bolletjes bolletje(s) in A: een hoorntje of B: een bakje? ")
    if houder == 'A':
        print(f'Dan krijgt u van mij een hoortje met {bolletjes} bolltjes')
    elif houder == 'B':
        print(f'Dan krijgt u van mij een bakje met {bolletjes} bolletjes')
    elif print('Sorry, dat snap ik niet...'):
        stap2()
    return houder

def stap3():
    bestellen = input('Hier is uw hoorntje/bakje met aantal bolletje(s).\n Wilt u nog meer bestellen?\n \n(Y/N)\n ')
    if bestellen == 'Y':
        stap1()
    elif bestellen == 'N':
        print('Bedankt en tot ziens!')
    else:
        print('Sorry dat snap ik niet...')
        stap3()

def extra(bolletjes):
    topping = ['A', 'C', 'M', 'V']
    for i in range(bolletjes):
        smaken = input('Welke smaak wilt u voor bolletje nummber?\n A: Aardbei\n C: Chocolade \n M: Munt \n V: Vanille\n')
    if smaken in topping:
        print('')
    else:
        print('sorry ik snap het niet')
    return

Bolletjes = 0
Horrentjes = 0
Bakjes = 0

Bolletjes = Bolletjes * 1,10
Horrentjes = Horrentjes * 1,25
Bakjes = Bakjes * 0,75

def topping():
    


    
