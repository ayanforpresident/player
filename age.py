age = input('How old are you?')
print('you are ' + str(age) + ' years old')

'''
baby, kid, young adult, adult, elder citizen
'''

if age < 3:
    print('You are a baby!')
elif age < 13:
    print('Whats up kid!')

elif age > 13 and age < 20:
    print('Do U play Fortnite?')

elif age > 20 and age < 75:
    print('Hows Ur day going sir?')

elif age >= 75 and age <= 100:
    print('do U remember back then when phones didnt exist?')

elif age > 100:
    print('Ur not real. If U ARE real than Gmail 937996@pdsb.net')