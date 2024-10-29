target = int(input("Enter a number between 0 and 1000\n")) 

if target<=0 or target>1000:
    print("Number is not from range 0  - 1000")
else:
    sum_even = 0
    #different way
    #for i in range(2,target + 1, 2):
    for i in range(1, target+1):
        if i % 2 == 0:
            sum_even += i
    
    print("Sum of even numbers is ", sum_even)
