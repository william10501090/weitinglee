code = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
anticode = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}


def RTA(roman):
    number = 0
    for i in range(0, len(roman) - 1):
        if code[roman[i]] >= code[roman[i+1]]:
            number += code[roman[i]]
        else:
            number -= code[roman[i]]
    number += code[roman[len(roman)-1]]
    return number


"""def reverseRTA(number):
    roman = ""
    while number >= 1000:
        roman += "M"
        number -= 1000
    if number >= 900:
        roman += "CM"
        number -= 900
    if number >= 500:
        roman += "D"
        number -= 500
        while number >= 100:
            roman += "C"
            number -= 100
    if number >= 400:
        roman += "CD"
        number -= 400
    while number >= 100:
        roman += "C"
        number -= 100
    if number >= 90:
        roman += "XC"
        number -= 90
    if number >= 50:
        roman += "L"
        number -= 50
        while number >= 10:
            roman += "X"
            number -= 10
    if number >= 40:
        roman += "XL"
        number -= 40
    while number >= 10:
        roman += "X"
        number -= 10
    if number >= 9:
        roman += "IX"
        number -= 9
    if number >= 5:
        roman += "V"
        number -= 5
        while number >= 1:
            roman += "I"
            number -= 1
    if number >= 4:
        roman += "IV"
        number -= 4
    while number >= 1:
        roman += "I"
        number -= 1
    return roman
"""

def antiRTA(number):
    roman = ""
    while number >= 1000:
        roman += "M"
        number -= 1000
    for dividing in [100, 10, 1]:
        res = int(number / dividing)
        if res == 4 or res == 9:
            roman += anticode[dividing] + anticode[(res + 1) * dividing]
            number -= dividing * res
        elif res >= 5:
            roman += anticode[5 * dividing]
            number -= dividing * 5
        while number >= dividing:
            roman += anticode[dividing]
            number -= dividing
    return roman


while True:
    _input = input()
    if _input != "#":
        a, b = _input.split( )
        ans = abs(RTA(a) - RTA(b))
        if ans == 0:
            print("ZERO")
        else:
            print(antiRTA(ans))
    else:
        exit()
