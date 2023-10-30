import random

# Definir opciones para el juego
options = ["rock", "paper", "scissors"]

# Función para que el jugador elija una opción
def get_player_choice():
    while True:
        choice = input("Choose rock, paper, or scissors: ").lower()
        if choice in options:
            return choice
        else:
            print("Invalid choice. Please choose again.")

# Función para que el oponente elija una opción aleatoria
def get_opponent_choice():
    return random.choice(options)

# Función para comparar las opciones y determinar el ganador
def get_round_result(player_choice, opponent_choice):
    if player_choice == opponent_choice:
        return "tie"
    elif player_choice == "rock" and opponent_choice == "scissors":
        return "win"
    elif player_choice == "paper" and opponent_choice == "rock":
        return "win"
    elif player_choice == "scissors" and opponent_choice == "paper":
        return "win"
    else:
        return "lose"

# Función para mostrar el resultado de la ronda y actualizar la puntuación
def play_round(score):
    player_choice = get_player_choice()
    opponent_choice = get_opponent_choice()
    result = get_round_result(player_choice, opponent_choice)
    if result == "tie":
        print(f"You both chose {player_choice}. It's a tie!")
    elif result == "win":
        print(f"You chose {player_choice} and the opponent chose {opponent_choice}. You win!")
        score["player"] += 1
    else:
        print(f"You chose {player_choice} and the opponent chose {opponent_choice}. You lose!")
        score["opponent"] += 1

# Función para preguntar al jugador si quiere jugar de nuevo
def play_again():
    while True:
        choice = input("Do you want to play again? (y/n): ").lower()
        if choice == "y":
            return True
        elif choice == "n":
            return False
        else:
            print("Invalid choice. Please choose again.")

# Función principal para ejecutar el juego
def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    score = {"player": 0, "opponent": 0}
    while True:
        play_round(score)
        print(f"Score: Player {score['player']} - Opponent {score['opponent']}")
        if not play_again():
            break
    print("Thanks for playing!")

# Ejecutar el juego
play_game()