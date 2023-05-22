def romanToInt(s):
    dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    minus = {'V': 'I', 'X': 'I', 'L': 'X', 'C': 'X', 'D':'C', 'M':'C',  'Z':'', 'I':''}
    str = list(s)[::-1]
    prev = 'Z'
    result = 0
    for l in str:
        if l == minus[prev]:
            result -= dict[l]
        else:
            result += dict[l]
        prev = l
    return result

s = "MCMXCIV"
print(romanToInt(s))