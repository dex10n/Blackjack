from blackjack import *
import os

print('Bienvenido a blackjack!')
jugando = comenzar_juego()
if jugando:
    fichas_jug = Fichas()
    fichas=definir_fichas()#Cantidad de fichas con las que arranca
    fichas_jug.cantidad = fichas
    while jugando:
        deck = Mazo()
        deck.embarajar()
        jugador = Mano()
        
        #Mejorar haciendo que apostar() reciba fichas (del tipo Fichas)
        while True:
            apuesta = fichas_jug.apuesta = apostar()
            if fichas_jug.cantidad<apuesta:
                print('Esa apuesta supera su cantidad de fichas')
                continue
            elif apuesta <= 0:
                print('Su apuesta debe ser mayor a 0')
                continue
            else:
                break

        c1_dealer, c2_dealer = cartas_dealer(deck)#cartas 1 y 2 del dealer 
        c1_jug, c2_jug = cartas_jugador(deck)#cartas 1 y 2 del jugador
        jugador.agregar_carta(c1_jug)#agrega cartas a la mano
        jugador.agregar_carta(c2_jug)
        show_dealer(c2_dealer)#muestra solo la carta 2 del dealer
        show_jugador(c1_jug, c2_jug)#muestra las 2 cartas del jugador

        
        #si el jugador tiene 21 de mano inicial y el dealer tambien hay empate
        #si sólo tiene 21 el jugador, gana éste
        if jugador.valor == 21:
            valor_dealer = valores[c1_dealer.tipo] + valores[c2_dealer.tipo]
            #empate1
            if valor_dealer == 21:
                print('\nHay un empate, cartas del dealer: ')
                print(c1_dealer)
                print(c2_dealer)
                print(f'\nSigue teniendo {fichas_jug.cantidad} fichas')

                again = replay()
                if again:
                    continue
                else:
                    break
            else:
                #ganar1
                fichas_jug.ganar()
                print(f'\nHas ganado {apuesta}, tienes {fichas_jug.cantidad} fichas')

                again = replay()
                if again:
                    continue
                else:
                    break

        #turno jugador
        valor_mano = hit_me(deck,jugador)

        #perder1
        if valor_mano > 21:
            fichas_jug.perder()
            print(f'\nHa perdido. Mano: {jugador.valor} puntos')
            
            if fichas_jug.cantidad > 0:
                print(f'\nLe quedan {fichas_jug.cantidad} fichas')

                again = replay()
                if again:
                    continue
                else:
                    break
            else:
                print('\nNo le quedan fichas. Fin del juego')
                break
        

        #turno dealer
        valor_dealer = turno_dealer(c1_dealer, c2_dealer, deck)
        
        #perder2 #igual que arriba, arreglar para no repetir código
        if valor_dealer > valor_mano and valor_dealer <= 21:
            fichas_jug.perder()
            print(f'\nHa perdido. Mano: {jugador.valor} puntos')

            if fichas_jug.cantidad > 0:
                print(f'\nLe quedan {fichas_jug.cantidad} fichas')

                again = replay()
                if again:
                    continue
                else:
                    break
            else:
                print('\nNo le quedan fichas. Fin del juego')
                break
        #empate2
        elif valor_dealer == valor_mano:
            print('\nHay un empate')
            print(f'Sigue teniendo {fichas_jug.cantidad} fichas')

            again = replay()
            if again:
                continue
            else:
                break
        #ganar2
        else:
            fichas_jug.ganar()
            print(f'\nHas ganado {apuesta}, tienes {fichas_jug.cantidad} fichas')

            again = replay()
            if again:
                continue
            else:
                break
    os.system('pause')