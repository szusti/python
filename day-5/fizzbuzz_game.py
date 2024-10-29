
for i in range(1,101):
    result = "0"
    if i % 3 == 0:
        result = "Fizz"
    if i % 5 == 0:
        if result == "Fizz":
            result += "Buzz"
        else: result = "Buzz"       
    if result == "0": 
        result = str(i)
    print(result)