# Browse the complete list of string methods at:
# https://docs.python.org/3/library/stdtypes.html#string-methods 
#and try them out here. Endeavor to copy the link without the first # comment sign beginning it.

x = 'It Will Get Better'

print(x.capitalize())

print(x.casefold())

print(x.center(30, '+'))

print(x.count('t', 0, 35))

print(x.encode())

print('I will encode this string to ascii'.encode('ascii'))

print(x.endswith('t', 0, 10))

print(x.endswith('t', 0, 11))

print('Big\tBigger\tBiggest\t'.expandtabs(10))

print(x.find('W'))

print(x.find('w'))

print('Do you believe Nigeria will get better? {}'.format('Yes, I believe.'))

def answer(par):
    ans = 'My name is {first_name} and I attend {church_name}'.format_map(par)
    return ans

par = {'first_name': 'Olaitan', 'church_name': 'Daystar Christian Center.' }
print(answer(par))


