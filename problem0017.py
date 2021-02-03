def tensToText(n):
    if n == 0:
        return "ten"
    elif n == 1:
        return "eleven"
    elif n == 2:
        return "twelve"
    elif n == 3:
        return "thirteen"
    elif n == 4:
        return "fourteen"
    elif n == 5:
        return "fifteen"
    elif n == 6:
        return "sixteen"
    elif n == 7:
        return "seventeen"
    elif n == 8:
        return "eighteen"
    elif n == 9:
        return "nineteen"

def decasToText(n):
    if n == 1:
        raise ValueError("1 is invalid")
    elif n == 2:
        return "twenty"
    elif n == 3:
        return "thirty"
    elif n == 4:
        return "forty"
    elif n == 5:
        return "fifty"
    elif n == 6:
        return "sixty"
    elif n == 7:
        return "seventy"
    elif n == 8:
        return "eighty"
    elif n == 9:
        return "ninety"
    elif n == 0:
        raise ValueError("0 is invalid")

def digitToText(n):
    if n == 1:
        return "one"
    elif n == 2:
        return "two"
    elif n == 3:
        return "three"
    elif n == 4:
        return "four"
    elif n == 5:
        return "five"
    elif n == 6:
        return "six"
    elif n == 7:
        return "seven"
    elif n == 8:
        return "eight"
    elif n == 9:
        return "nine"
    elif n == 0:
        return ""

def numberToText(n):
    milles = n // 1000
    hectos = n % 1000 // 100
    decas = n % 100 // 10
    ones = n % 10
    s = ""
    if milles > 0:
        s += digitToText(milles) + " thousand"
    if hectos > 0:
        if s != "":
            s += " and "
        s += digitToText(hectos) + " hundred"
    if decas > 1:
        if s != "":
            s += " and "
        s += decasToText(decas) + " "
    elif decas == 1:
        if s != "":
            s += " and "
        s += tensToText(ones)
        return s

    if (hectos > 0 or milles > 0) and decas == 0 and ones > 0:
        s += " and "

    s += digitToText(ones)
    return s

s = 0
for i in range(1, 1001):
    s += len(numberToText(i).replace(" ", ""))
print(s)