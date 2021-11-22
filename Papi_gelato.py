def stap1():
    print('Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.')
    aantal = input('Hoeveel bolletjes wilt u? ')
    if aantal <= '3':
        print(f'Dan krijgt u van mij {aantal} bolletjes')
    elif aantal <= '8':
        print(f'Dan krijgt u van mij {aantal} bolletjes')
    elif aantal > '8':
        print('Sorry, zulke grote bakken hebben we niet')
        aantal = stap1()
    return aantal

def stap2():
    aantal = stap1()
    houder = input("Wilt u deze aantal bolletje(s) in A: een hoorntje of B: een bakje? ")
    if houder == 'A':
        print(f'Dan krijgt u van mij een hoortje met {aantal}')
    elif houder == 'B':
        print(f'Dan krijgt u van mij een bakje met {aantal}')
    elif print('Sorry, dat snap ik niet...'):
        stap2()
    return 

def stap3():
    bestellen = input('Hier is uw hoorntje/bakje met aantal bolletje(s).\n Wilt u nog meer bestellen?\n \n(Y/N)\n ')
    if bestellen == 'Y':
        stap1()
    elif bestellen == 'N':
        print('Bedankt en tot ziens!')
    else:
        print('Sorry dat snap ik niet...')
        stap3()

def extra():
    topping = ['A', 'C', 'M', 'V']
    for i in range(3):
        smaken = input('Welke smaak wilt u voor bolletje nummber?\n A: Aardbei\n C: Chocolade \n M: Munt \n V: Vanille\n')
    if smaken in topping:
        print('')
    else:
        print('sorry ik snap het niet')
    return

