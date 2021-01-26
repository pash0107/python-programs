def getCount(inputStr):
    num_vowels = 0
    num_vowels = len([num_vowels for char in inputStr if char in "aeiou"])
    
    return num_vowels