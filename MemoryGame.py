# Will generate a list of random numbers between 1 to 101. The list length will be difficulty.
def generate_sequence(difficulty):
    from random import seed
    from random import randint
    list1 = []
    for number in range(difficulty):
        list1.append(int(randint(1, 101)))
    return(list1)

# Will return a list of numbers prompted from the user. The list length  will be in the size of difficulty.
def get_list_from_user(difficulty):
    list2 = []
    for number in range(difficulty):
        list2.append(int(input()))
    return (list2)

# A function to compare two lists if they are equal. The function will return  True / False.
def is_list_equal(list1, list2):
    if list1 == list2:
        return True
    else:
        return False

# Will call the functions above and play the game. Will return True / False if the user lost or won.
def playMemory(difficulty):
    import os
    import time
    list1=generate_sequence(difficulty)
    print(list1)
    time.sleep(7) # wait 7 sec
    os.system('cls') # clear screen
    print("now type the numbers you saw")
    list2=get_list_from_user(difficulty)
    return(is_list_equal(list1, list2))

