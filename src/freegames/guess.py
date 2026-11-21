from random import randint
start =1
end =100
value =randint (start ,end )
print ("Я загадал число от",start ,'до',end )
guess =None
while guess !=value :
    text =input ('Угадайте число: ')
    guess =int (text )
    if guess <value :
        print ('Больше.')
    elif guess >value :
        print ('Меньше.')
print ('Поздравляю! Вы угадали правильный ответ:',value )