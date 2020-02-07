# Will get the current currency rate from USD to ILS and will generate an interval as follows:
# a. for given difficulty d, and total value of money t the interval will be: (t - (5 - d), t + (5 - d))
def get_money_interval(difficulty, total):
    return(total - (5 - difficulty), total + (5 - difficulty))

def get_currency():
    import requests
    import json

    url = "https://api.exchangeratesapi.io/latest?symbols=USD,ILS"

    response = requests.get(url)
    data = response.text
    parsed = json.loads(data)

    return(int(parsed["rates"]["ILS"]))

#- A method to prompt a guess from the user to enter a guess of value to a given amount of USD
def get_guess_from_user():
    print("Enter a guess of total amount USD")
    return(input(int()))

# Will call the functions above and play the game. Will return True / False if the user lost or won.
def playCurrency(difficulty):
    from random import seed
    from random import randint
    num = int(randint(1,100))
    currency = get_currency()
    total = int(num*currency)
    check = get_money_interval(difficulty, total)
    user_guess = get_guess_from_user()
    if int(user_guess) >= int(check[0]) and int(user_guess) <= int(check[1]):
        return True
    else:
        return False
    
    print("test")
