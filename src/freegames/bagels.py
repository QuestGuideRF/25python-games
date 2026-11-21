from random import sample ,shuffle
digits =3
guesses =10
print ('Я загадал',digits ,'значное число.')
print ('Попробуйте угадать его.')
print ('Вот подсказки:')
print ('Когда я говорю:    Это значит:')
print ('  pico         Одна цифра правильная, но не на своем месте.')
print ('  fermi        Одна цифра правильная и на своем месте.')
print ('  bagels       Нет правильных цифр.')
print ('В числе нет повторяющихся цифр.')
letters =sample ('0123456789',digits )
if letters [0 ]=='0':
    letters .reverse ()
number =''.join (letters )
print ('Я загадал число.')
print ('У вас есть',guesses ,'попыток, чтобы угадать его.')
counter =1
while True :
    print ('Попытка №',counter )
    guess =input ()
    if len (guess )!=digits :
        print ('Неверное количество цифр. Попробуйте снова!')
        continue
    clues =[]
    for index in range (digits ):
        if guess [index ]==number [index ]:
            clues .append ('fermi')
        elif guess [index ]in number :
            clues .append ('pico')
    shuffle (clues )
    if len (clues )==0 :
        print ('bagels')
    else :
        print (' '.join (clues ))
    counter +=1
    if guess ==number :
        print ('Вы угадали!')
        break
    if counter >guesses :
        print ('У вас закончились попытки. Ответ был',number )
        break