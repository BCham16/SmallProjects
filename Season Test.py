input_month = input()
input_day = int(input())
season = ''

#make a list of valid months for input_month to check against
valid_months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
'November', 'December']

#make sure capitalization doesn't throw false invalid for month string
input_month = input_month.capitalize()

#check for invalid inputs
if int(input_day) > 31 or input_month not in valid_months:
    print('Invalid')
    quit()
if (input_month == 'September' or input_month == 'April' or input_month == 'June' or input_month == 'November') and (int(input_day) > 30):
    print('Invalid')
    quit()
if input_month == 'February' and int(input_day) > 28:
    print('Invalid')
    quit()
if int(input_day) < 1:
    print('Invalid')
    quit()

#Jan & Feb (full month winter)
if input_month == 'January' or input_month == 'February':
    season = 'Winter'

#March (split winter/spring)
if input_month == 'March':
    if input_day <= 19:
        season = 'Winter'
    else:
        season = 'Spring'

#April & May (full month spring)
if input_month == 'April' or input_month == 'May':
    season = 'Spring'

#June (split spring/summer)
if input_month == 'June':
    if input_day <= 20:
        season = 'Spring'
    else:
        season = 'Summer'
            
#July & August (full month summer)
if input_month == 'July' or input_month == 'August':
    season = 'Summer'
    
#September (split summer/fall)
if input_month == 'September':
    if input_day <= 21:
        season = 'Summer'
    else:
        season = 'Autumn'
            
#October & November (full month fall)
if input_month == 'October' or input_month == 'November':
    season = 'Autumn'
    
#December (split fall/winter)
if input_month == 'December':
    if input_day <= 21:
        season = 'Autumn'
    else:
        season = 'Winter'
  
#final output
print(season)