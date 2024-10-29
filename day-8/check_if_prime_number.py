def prime_checker(number):
    what_numbers_divide = []
    for i in range(number,1,-1):
        if number % i == 0:
            what_numbers_divide.append(i)
    print("Jakie liczby sa podzielne\n",what_numbers_divide)
    how_many_numbers = len(what_numbers_divide)
    print (f"Your number divides by {how_many_numbers} numbers")
    if how_many_numbers == 2:
        print("Your number is prime")
    else:
        print("Your number is not prime")

n = int(input())
prime_checker(number=n)

