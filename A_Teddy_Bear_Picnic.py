def bears(n):
    if n == 42: #ends the rcursion with a true
        return True
    if n < 42: #ends the recursion with a false
        return False
    if n%5 == 0:
        return bears(n - 42)
    list = []
    for letter in str(n): #makes a list so I can find the last two numbers when mod 3 and mod 4 ==0
        list.append(letter)
    if n%3 == 0 and int(list[len(list) - 1]) * int(list[len(list) - 2]) != 0: # second part of and statement make sure value is not 0
        return bears(n - int(list[len(list)-1]) * int(list[len(list)-2])) #multiplies last two numbers of integer and calls bears() recursively
    if n % 4 == 0 and int(list[len(list) - 1]) * int(list[len(list) - 2]) != 0:
        return bears(n - int(list[len(list) - 1]) * int(list[len(list) - 2]))
    if n%2 == 0:
        return bears(n//2)
    return False #returns false if nothing is satisfied