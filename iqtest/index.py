  
def iq_test(string):
    #your code here

    numbers = string.split()
    noOdds = 0
    noEvens = 0
    position = 0

    for i in range (0, len(numbers)):
        if(int(numbers[i]) % 2 == 0):
            noEvens = noEvens + 1
        else:
            noOdds = noOdds + 1

    if(noOdds > noEvens):
        for i in range(0, len(numbers)):
            if (int(numbers[i]) % 2 == 0):
                position = i+1
    else:
        for i in range(0, len(numbers)):
            if (int(numbers[i]) % 2 != 0):
                position = i+1
    return position