def solution(n):
    value = 0
    romanStr = ""
    index = 0
    roman = [
        {'M': 1000},
        {'CM': 900},
        {'D': 500},
        {'CD': 400},
        {'C': 100},
        {'XC': 90},
        {'L': 50},
        {'XL': 40},
        {'X': 10},
        {'IX': 9},
        {'V': 5},
        {'IV': 4},
        {'I': 1}
    ]
    while index < len(roman):
        for key in roman[index]:
            while value + roman[index][key] <= n:
                value += roman[index][key]
                romanStr += key
        index += 1
    
    return romanStr
        
print(solution(786))