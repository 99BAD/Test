import random
#yutyifgkuhlikj

#ajout Fati
def computer_guess(x):
    low = 1
    high = x
    k =''
    while k != 'c':
        guess= random.randint(low,high)
        k = input(f'{guess} Too high? (H) Too low? (L) Correct? (C)').lower
        if k == 'l':
            high = guess-1
            print(high)
        elif k =='h':
            low = guess+1
            print(low)
    
    print(f'valeur trouvée {guess}')


computer_guess(20)