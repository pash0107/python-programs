def hello():
    return 'Hi Fuck!'

def other(some_func):
    print('Others')
    print(some_func())

# print(hello()) #printing hello function return
# print(hello) #parent function

print(other(hello)) #t0 get other funtion