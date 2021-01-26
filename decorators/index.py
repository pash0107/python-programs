def hello(name='Joshua'):
    print('The hello() funcition has been executed!')

    def greet():
        return '\t This is the greet() func inside hello!'
    
    def welcome():
        return '\t This is welcome() func inside hello!'

    print('Return Function')

    if name == 'Joshua':
        return greet
    else:
        return welcome

def cool():
    
    def super_cool():
        return 'Super fuck'

    return super_cool

some_func = cool()
print(some_func) #parent
print(some_func()) #child function

new_func = hello('Joshua')

print(new_func())