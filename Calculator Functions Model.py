# Calculator Functions model

def decimal_cal():
    """The function that handles the decimal part of the calculator"""

    valA = int(input(""))
    sign = input("")
    valB = int(input(""))


    if sign == "+":
        result = valA + valB
    elif sign == "-":
        result = valA - valB
    elif sign == "x":
        result = valA * valB
    elif sign == "/":
        result == valA / valB

    return result
