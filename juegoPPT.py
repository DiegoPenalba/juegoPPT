# Desafio
# se puede colocar el nombre en la segunda solicitud
# lo ingresado por el usuario sea lowercase de tal forma de comparar minuscula con minuscula
# mas de 1 tuno en bucle while

nombreJugador1 = input("Ingrese el nombre del jugador 1: ")
nombreJugador2 = input("Ingrese el nombre del jugador 2: ")

jugarDeNuevo = True

while jugarDeNuevo:
    eleccionJugador1 = input(f"{nombreJugador1}, elige piedra, papel o tijera: ").lower()
    eleccionJugador2 = input(f"{nombreJugador2}, elige piedra, papel o tijera: ").lower()

    condicion1 = eleccionJugador1 == "piedra" and eleccionJugador2 == "tijera"
    condicion2 = eleccionJugador1 == "tijera" and eleccionJugador2 == "papel"
    condicion3 = eleccionJugador1 == "papel" and eleccionJugador2 == "piedra"

    if condicion1 or condicion2 or condicion3:
        print(f"{nombreJugador1} gana!")
    elif eleccionJugador1 == eleccionJugador2:
        print("Es un empate!")
    else:
        print(f"{nombreJugador2} gana!")

    continuar = input("¿Desean jugar otra vez? (si/no): ").lower()
    if continuar != "si":
        print("Gracias por jugar!")
        jugarDeNuevo = False
    else:
        print("¡Comencemos de nuevo!")

