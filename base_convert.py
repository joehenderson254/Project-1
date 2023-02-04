def convert(num, b):
    """Recursive function that returns a string representing num in the base b"""
    if num == 0:
        return ""
    remainder = str(num % b)
    if num%b == 10:
        remainder = "A"
    elif num%b == 11:
        remainder = "B"
    elif num%b == 12:
        remainder = "C"
    elif num%b == 13:
        remainder = "D"
    elif num%b == 14:
        remainder = "E"
    elif num%b == 15:
        remainder = "F"
    return convert(num//b, b) + remainder #recursively calls convert() adding new remainder value to beginning