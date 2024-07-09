import string

def length_case(password):
    if len(password) < 8:
        strength = 0
        score -= 2
    elif len(password) >= 8:
        strength = 1
    return strength

score = 10
print()
print('Please give the password!!!')
print()
password = input('Password: ')

upper_case = any([1 if c in string.ascii_uppercase else 0 for c in password])

lower_case = any([1 if c in string.ascii_lowercase else 0 for c in password])

digit_case = any([1 if c in string.digits else 0 for c in password])

spec_char_case = any([1 if c in string.punctuation else 0 for c in password])

if length_case == 0:
    print('Your password is too short')
    score -= 2

if upper_case == False:
    print('Please use at least one upper letter')
    score -= 2

if lower_case == False:
    print('Please use at least one lower letter')
    score -= 2

if digit_case == False:
    print('Please use at least one digit')
    score -= 2

if spec_char_case == False:
    print('Please use at least one special char')
    score -= 2

print(f'Your password score is {score}')



