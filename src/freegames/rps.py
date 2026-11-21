import random
beats ={'r':'s','p':'r','s':'p'}
loses ={value :key for key ,value in beats .items ()}
state ={'player':0 ,'computer':0 ,'ties':0 }
guesses =[]
default =random .choice ('rps')
def always_same ():
    return default
def random_strategy ():
    return random .choice ('rps')
def beat_last ():
    if not guesses :
        return default
    last ,_ =guesses [-1 ]
    return loses [last ]
strategies =[always_same ,random_strategy ,beat_last ]
strategy =random .choice (strategies )
def get_option ():
    while True :
        choice =input ('Введите "r" для камня, "p" для бумаги, "s" для ножниц: ')
        if choice not in beats :
            print ('Неверный выбор.')
            continue
        return choice
print (__doc__ )
while True :
    player =get_option ()
    computer =strategy ()
    guess =(player ,computer )
    guesses .append (guess )
    print ('Игрок выбирает:',player )
    print ('Компьютер выбирает:',computer )
    if player ==computer :
        state ['ties']+=1
        print ('Ничья!')
    elif beats [player ]==computer :
        state ['player']+=1
        print ('Игрок выигрывает!')
    else :
        state ['computer']+=1
        print ('Компьютер выигрывает!')
    print ()
    print ('Очки игрока:',state ['player'])
    print ('Очки компьютера:',state ['computer'])
    print ()
    if state ['player']==5 :
        print ('ИГРОК ВЫИГРАЛ!')
        break
    if state ['computer']==5 :
        print ('КОМПЬЮТЕР ВЫИГРАЛ!')
        break
print ('Стратегия компьютера:',strategy .__name__ )