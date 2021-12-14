def papi_gelato():
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