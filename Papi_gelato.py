def stap1():
    print('Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.')
    aantal = input('Hoeveel bolletjes wilt u? ')
    if aantal <= '3':
        print('Dan krijgt u van mij ' + aantal + ' bolletjes')
    elif aantal <= '8':
        print('Dan krijgt u van mij ' + aantal + ' bolletjes')
    elif aantal > '8':
        print('Sorry, zulke grote bakken hebben we niet')
        stap1()
    return

def stap2():
    houder = input("Wilt u deze aantal bolletje(s) in A: een hoorntje of B: een bakje? ")
    if houder == 'A':
        print('Dan krijgt u van mij een hoortje')
    elif houder == 'B':
        print('Dan krijgt u van mij een bakje')
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

stap1()
stap2()
stap3()
