def generate_number(difficulty):
    from random import seed
    from random import randint
    return (randint(1, difficulty))

def get_guess_from_user(difficulty):
    print("Guess a number between 1 to", difficulty)
    return int(input())

def compare_results(num, secret_number):
    if num == secret_number:
        return True
    else:
        return False

def playGuessGame(difficulty):
    num=get_guess_from_user(difficulty)
    secret_number = generate_number(difficulty)
    return(compare_results(num, secret_number))