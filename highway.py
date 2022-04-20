highway_number = int(input('Enter a highway number: '))
priaux = ''
direction = ''
serving = 0

if highway_number > 99:
    priaux = 'auxiliary'
    serving = highway_number % 100
else:
    priaux = 'primary'
if highway_number % 2 == 0:
    direction = 'east/west'
else:
    direction = 'north/south'


if highway_number < 1 or highway_number > 999:
    print(str(highway_number)+' is not a valid interstate highway number.')
elif highway_number > 99:
    print('I-'+str(highway_number)+' is '+priaux+', serving I-'+str(serving)+', going '+direction+'.')
else:
    print('I-'+str(highway_number)+' is '+priaux+', going '+direction+'.')
    
