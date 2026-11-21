def encrypt (message ,key ):
    result =''
    for letter in message :
        if letter .isalpha ():
            num =ord (letter )
            if letter .isupper ():
                base =ord ('A')
            else :
                assert letter .islower ()
                base =ord ('a')
            num =(num -base +key )%26 +base
            result +=chr (num )
        elif letter .isdigit ():
            result +=letter
        else :
            result +=letter
    return result
def decrypt (message ,key ):
    return encrypt (message ,-key )
def decode (message ):
    pass
def get_key ():
    try :
        text =input ('Введите ключ (1 - 25): ')
        key =int (text )
        return key
    except :
        print ('Неверный ключ. Используется ключ: 0.')
        return 0
print ('Вы хотите зашифровать, расшифровать или декодировать сообщение?')
choice =input ()
if choice =='encrypt':
    phrase =input ('Сообщение: ')
    code =get_key ()
    print ('Зашифрованное сообщение:',encrypt (phrase ,code ))
elif choice =='decrypt':
    phrase =input ('Сообщение: ')
    code =get_key ()
    print ('Расшифрованное сообщение:',decrypt (phrase ,code ))
elif choice =='decode':
    phrase =input ('Сообщение: ')
    print ('Декодирование сообщения:')
    decode (phrase )
else :
    print ('Ошибка: Неопознанная команда')