import time

fila = ['Momo', 'Coscu']
cont = 1 
print('- Hola, bienvenido al comando de la aereonave!')

while cont > 0:
    def vuelo():
        op1 = input('- Tienes un nuevo pasajero, deseas dejarlo entrar? (S o N): ')
        if op1 == 'S' or op1 == 's':
            fila.append(input('- Ingresa el nombre del nuevo abordante: '))
            time.sleep(1)
            print('- Muy bien, tu fila cuenta con un nuevo pasajero!')
            True
        elif op1 == 'N' or op1 == 'n': 
            time.sleep(1)
            print('- Uh que lastima, tu fila queda asi: ',fila)
            False
        else:
            print('- Ingresa una letra valida rey!')
    vuelo()

    value = input('- Cierras las puertas de la aereonave? si dices que si, no entrara mas nadie! (S o N): ')
    if value == 'N' or value == 'n':
        time.sleep(1)
        print('- Oka, sigamos sumando gente!')
        vuelo()
        cont = 1
    elif value == 'S' or value == 's': 
        time.sleep(1)
        print('- Que pena, tu Splinterneta quedo asi: ', fila)
        cont = 0
    else:
        print('- Ingresa una letra valida rey!') 

