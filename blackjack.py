import random

palos = ['pica', 'corazon', 'espada', 'diamante']
tipos = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jota', 'Reina', 'Rey', 'As']
valores = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jota':10, 'Reina':10, 'Rey':10, 'As':11}

class Carta:
    def __init__(self, palo, tipo):
        self.tipo = tipo
        self.palo = palo

    def __str__(self):
        return self.tipo + ' de ' + self.palo

class Mazo:
    def __init__(self):
        self.mazo = []
        for palo in palos:
            for tipo in tipos:
                self.mazo.append(Carta(palo, tipo))
    
    def __str__(self):
        comp_mazo = ''
        for car in self.mazo:
            comp_mazo += str(car) + ' '
        return comp_mazo

    def embarajar(self):
        random.shuffle(self.mazo)

    def repartir(self):
        return self.mazo.pop()


class Mano:
    def __init__(self):
        self.cartas = []
        self.valor = 0
        self.ases = 0

    def agregar_carta(self,carta):
        self.cartas.append(carta)
        self.valor += valores[carta.tipo]
        if carta.tipo == 'As':
            self.ases += 1

    def valor_ases(self):
        while self.valor > 21 and self.ases > 0:
            self.valor -= 10
            self.ases -= 1
    
class Fichas:
    def __init__(self,cantidad=0):
        self.cantidad = cantidad
        self.apuesta = 0

    def ganar(self):
        self.cantidad += self.apuesta

    def perder(self):
        self.cantidad -= self.apuesta

def definir_fichas():
    while True:
        try:
            cant_fichas=int(input('\nCon cuántas fichas desea comenzar a jugar? '))
        except:
            print('\nError: debe ingresar un número')
        else:
            if cant_fichas<=0:
                print('\nDebe ingresar un número mayor a 0')
                continue
            break
    return cant_fichas

def apostar():#cant_fichas
    cant_apuesta=0
    while True:
        try:
            cant_apuesta = int(input('\nIngrese cantidad a apostar: '))
        except:
            print('\nError: debe ingresar un número')
        else:
            break
    return cant_apuesta

def comenzar_juego():
    resp = ''
    while resp != 's' and resp != 'n':
        resp = input('\nDesea comenzar el juego? "S" o "N": ').lower()
    if resp == 's':
        return True
    else:
        return False

def cartas_dealer(deck):
    carta1_dealer = deck.repartir()
    carta2_dealer = deck.repartir()
    return carta1_dealer, carta2_dealer

def cartas_jugador(deck):
    carta1_jug = deck.repartir()
    carta2_jug = deck.repartir()

    return carta1_jug, carta2_jug

def show_dealer(carta2):
    print('\nCartas del dealer:')
    print('Carta oculta')
    print(f'{carta2}')

def show_jugador(carta1,carta2):
    print('\nSus cartas:')
    print(f'{carta1}')
    print(f'{carta2}')

#Mejorar haciendo que sólo agregue la carta a la mano y haga el ajuste
# de ases. Pasar el control del while loop al archivo2 o a otra funcion 
def hit_me(deck, mano):
    while True:
        resp = ''
        while resp != 's' and resp != 'n':
            resp = input('\nQuiere otra carta? "S" o "N": ')
        if resp == 's':
            carta = deck.repartir()
            mano.agregar_carta(carta)
            print(carta)
            mano.valor_ases()
            if mano.valor > 21:
                break
            elif mano.valor == 21:
                break
            else:
                continue
        else:
            break    
    return mano.valor

#mejorarlo asignandole Mano como al jugador o haciendole el control de ases 
#en esta misma función
def turno_dealer(carta1, carta2, deck):
    print('\nCartas del dealer:')
    print(carta1)
    print(carta2)
    valor = valores[carta1.tipo] + valores[carta2.tipo]
    while valor <= 17:
        carta = deck.repartir()
        print(f'\nRoba...\n{carta}')
        valor += valores[carta.tipo]
    return valor

def replay():
    sigue = ''
    while sigue != 's' and sigue != 'n':
        sigue = input('\nDesea seguir jugando? "S" o "N": ').lower()
    return sigue == 's'