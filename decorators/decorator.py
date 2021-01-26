def new_decorator(fuckoff):

    def wrap_func():
        
        print('Some extra code before the orig function')
        fuckoff()
        print('After the orig function')
    
    return wrap_func

@new_decorator
def func_needs_decorator(): #fuckoff() function

    print('I want to be decorated')

#original_func() will be the bridge to execute decorator

decorated_function = new_decorator(func_needs_decorator) #long method

print(decorated_function())