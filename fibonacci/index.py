def gen_fib(n):

    a = 1
    b = 1
    output = []
    for i in range(n):
        yield a #least memory loads
        # output.append(a) #long method
        a,b = b, a+b

for number in gen_fib(10):
    print('{} '.format(number))
