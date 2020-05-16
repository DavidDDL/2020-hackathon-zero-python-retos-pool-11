from random import randint

options = ["Piedra", "Papel", "Tijeras"]

# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'
def quienGana(player, ai):
    player = player.capitalize()
    ai = ai.capitalize()
    if player == ai:
        return 'Empate!'
    elif player == "Piedra" and ai == "Papel":
        return 'Perdiste!'
    elif player == "Piedra" and ai == "Tijeras":
         return 'Ganaste!'
    elif player == "Papel" and ai == "Piedra":
         return 'Ganaste!'
    elif player == "Papel" and ai == "Tijeras":
         return 'Perdiste!'
    elif player == "Tijeras" and ai == "Piedra":
         return 'Perdiste!'
    elif player == "Tijeras" and ai == "Papel":
         return 'Ganaste!'

# Entry Point
def Game():
    #
    #
    #
    #
    player = input("Selecciona opción: 1 - Piedra, 2 - Papel, 3 - Tijeras: " )
    player = int(player)-1
    eleccion = options[player]
    print("Has elegido: " + eleccion)
    ai = randint(1,3)-1
    eleccionai = options[ai]
    print("AI elegido: " + eleccionai)
    player = eleccion
    ai = eleccionai
    winner = quienGana(player, ai)
    print(winner)