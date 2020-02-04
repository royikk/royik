def welcome(name):
    return ("Hello " + name + " and welcome to the World of Games (WoG). \nHere you can find many cool games to play.")

def load_game():
    from CurrencyRouletteGame import playCurrency
    from GuessGame import playGuessGame
    from MemoryGame import playMemory
    print("Please choose a game to play:\n\
    1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n\
    2. Guess Game - guess a number and see if you chose like the computer\n\
    3. Currency Roulette - try and guess the value of a random amount of USD in ILS")
    game=int(input())
    while (game < 1) or (game > 3):
        game=int(input("Wrong selection, please choose game to play from 1 to 3:"))

    difficulty=int(input("Please choose game difficulty from 1 to 5: "))
    while (difficulty < 1) or (difficulty > 5):
        difficulty=int(input("Wrong selection, please choose game difficulty from 1 to 5: "))
    if game == 1:
        playMemory(difficulty)
    elif game == 2:
        playGuessGame(difficulty)
    else:
        playCurrency(difficulty)

