#ex 1.1
number_of_day = int(input('Enter the days number: '))
if number_of_day == 0:
    print('Sunday')
elif number_of_day == 1:
    print('Monday')
elif number_of_day == 2:
    print('Tuesday')
elif number_of_day == 3:
    print('Wednesday')
elif number_of_day == 4:
    print('Thursday')
elif number_of_day == 5:
    print('Friday')
elif number_of_day == 6:
    print('Saturday')
else:
    print("Out of week days range.")

#ex 1.2 
######
days_of_week = {0:'Sunday', 1:'Monday', 2:'Tuesday', 3:'Wednesdya', 4:'Thursday', 5:'Friday', 6:'Saturday'}
num = int(input('Enter some number: '))
print(days_of_week[num])


#ex 2
text = input('Enter smth: \n')
if ' ' in text:
    print('There is a space in the text.')
else:
    print('There is no space in the text.')

# #ex 3
word = input('Enter the word: \n')
if word.endswith(word, 0, 2):
    print(word)
elif word.endswith('ing'):
    print(word + 'ly')
else:
    print(word + 'ing')


# #ex 4
year = int(input('Enter some year: \n'))
if year % 4 != 0:
    print('The year is not leap')
elif year % 100 != 0:
    print('The year is leap')
elif year % 400 == 0:
    print('The year is leap')
else:
    print('The year is not leap')
    
#ex 5 
print('Hello world')
