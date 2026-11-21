template ='|1| |2| |3| |4| через |5| |6|.'
parts ={
'1':'прилагательное',
'2':'прилагательное',
'3':'существительное',
'4':'глагол',
'5':'прилагательное',
'6':'существительное',
}
chunks =[]
for chunk in template .split ('|'):
    if chunk in parts :
        description =parts [chunk ]
        prompt ='Введите [{}]: '.format (description )
        word =input (prompt )
        chunks .append (word )
    else :
        chunks .append (chunk )
print ('='*80 )
story =''.join (chunks )
print (story )